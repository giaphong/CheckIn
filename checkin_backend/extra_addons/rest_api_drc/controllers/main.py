# -*- coding: utf-8 -*-
import json
from odoo import http, _
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class RestAPI(http.Controller):

    @http.route([
        '/api/user/get_token',
    ], auth="public", website=True, methods=['GET'])
    def get_token(self, **post):
        """
            Odoo requires users of the API to be authenticated before they can use any other API.
            Authentication itself is done through the authenticate function and returns Token.
            On Every API call user must send a token to Access any API.
            eg.localhost:8069/api/user/get_token?login=admin&password=admin
        """
        res = {}
        uid = request.session.authenticate(request.session.db, request.params[
            'login'], request.params['password'])
        if uid:
            user = request.env['res.users'].sudo().browse(uid)
            if not user.token:
                token = user.get_user_access_token()
                user.token = token
            res['token'] = user.token
            res['name'] = user.name
            res['login'] = user.login
            res['uid'] = uid
            request.session.logout()
            return json.dumps({'success': res})
        else:
            res['error'] = "Wrong login/password"
            return json.dumps(res)

    @http.route([
        '/api/user/reset_password',
    ], auth="public", website=True, methods=['GET'])
    def reset_password(self, **post):
        """
            Odoo requires users of the API to be authenticated before they can use any other API.
            Authentication itself is done through the authenticate function and returns Token.
            On Every API call user must send a token to Access any API.
            eg.localhost:8069/api/user/reset_password?login=admin&password=admin
        """
        try:
            res = {}
            if request.params.get('login'):
                current_user = request.env['res.users'].sudo().search(
                    [('login', '=', request.params.get('login'))])
            if not current_user:
                return json.dumps({'error': _('Invalid login')})
            user = request.env['res.users'].sudo().browse(current_user.id)
            user.write({'password': request.params['password']})
            res['message'] = 'Change password successfully'
            return json.dumps(res)
        except Exception as e:
            return json.dumps({'error': _(' %s' % e)})

    @http.route([
        '/api/user/delete_token',
    ], auth="public", website=True, methods=['GET'])
    def delete_token(self, **post):
        """
            Delete token : it is medetory to pass token after this call token will be deleted.
            eg.localhost:8069/api/user/delete_token?token=24e635ff9cc74429bed3d420243f5aa6
        """
        current_user = False
        if post.get('token'):
            current_user = request.env['res.users'].sudo().search(
                [('token', '=', post.get('token'))])
        if not current_user:
            return json.dumps({'error': _('Invalid User Token')})
        else:
            try:
                current_user.token = False
            except Exception as e:
                return json.dumps({'error': _(' %s' % e)})

        return json.dumps({'success': _('Token \'%s\' Deleted Successfully' % post.get('token'))})

    @http.route([
        '/api/user/refresh_token',
    ], auth="public", website=True, methods=['GET'])
    def refresh_token(self, **post):
        """
            Refresh token : it is medetory to pass token after this call token will return new token.
            eg.localhost:8069/api/user/refresh_token?token=24e635ff9cc74429bed3d420243f5aa6

            It return {"token": "6656a5ba22ca440ca53fd40caeea38eb"}
        """
        current_user = False
        if post.get('token'):
            current_user = request.env['res.users'].sudo().search(
                [('token', '=', post.get('token'))])
        if not current_user:
            return json.dumps({'error': _('Invalid User Token')})
        else:
            try:
                current_user.token = False
                token = current_user.get_user_access_token()
                current_user.token = token
                return json.dumps({'token': token})
            except Exception as e:
                return json.dumps({'error': _(' %s' % e)})

    @http.route(['/api/<string:model>/search', '/api/<string:model>/search/<int:id>'
                 ], type='http', auth="public")
    def search_data(self, model=None, id=None, **post):
        """
            list records , it is medetory to pass model name
            if id is pass with url then return a single record of a specific id Found
            else check domain in post data , if domain is found then return matched records
            else return all the data with id and name field.

            By default a search will return the ids and name of all records matching the
            condition, which may be a huge number.if offset and limit parameters
            are available to only retrieve a subset of all matched records.

            eg. for single record
            localhost:8069/api/res.partner/search/1?token=24e635ff9cc74429bed3d420243f5aa6
            eg. for search using domain, offset and limit
            localhost:8069/api/res.partner/search?token=24e635ff9cc74429bed3d420243f5aa6&domain=[('id', '>=', 7)]&offset=10&limit=5

            By default a search will return the ids and name of all records matching the condition,
            it may possible that also you want to read other fields name with than name and ids.
            Note: it will always returns id as default field name if field name
            is not given it will return (id and name) otherwise it will return (id and all given fields name).
        """
        result = dict()
        current_user = False
        if post.get('token'):
            current_user = request.env['res.users'].sudo().search(
                [('token', '=', post.get('token'))])
        if not current_user:
            return json.dumps({'error': _('Invalid User Token')})
        try:
            Model = request.env[model].sudo(current_user.id)
        except Exception as e:
            return json.dumps({'error': _('Model Not Found %s' % e)})
        else:
            if id:
                domain = [('id', '=', id)]
                fields = ['id', 'name']
                if post.get('fields'):
                    fields = eval(post.get('fields'))
            else:
                domain = post.get('domain') and eval(post['domain']) or []
                fields = ['name']
                if post.get('fields'):
                    fields = eval(post.get('fields'))

            result = Model.search_read(domain, fields=fields, offset=int(
                post.get('offset', 0)), limit=post.get('limit') and int(post['limit'] or None),
                                       order=post.get('order') or None)
        return json.dumps(result)

    @http.route(['/api/<string:model>/search_ids'
                 ], type='http', auth="public")
    def search_ids(self, model=None, id=None, **post):
        """
            list records , it is medetory to pass model name
            if id is pass with url then return a single record of a specific id Found
            else check domain in post data , if domain is found then return matched records
            else return all the data with id and name field.

            By default a search will return the ids and name of all records matching the
            condition, which may be a huge number.if offset and limit parameters
            are available to only retrieve a subset of all matched records.

            eg. for single record
            localhost:8069/api/res.partner/search/1?token=24e635ff9cc74429bed3d420243f5aa6
            eg. for search using domain, offset and limit
            localhost:8069/api/res.partner/search?token=24e635ff9cc74429bed3d420243f5aa6&domain=[('id', '>=', 7)]&offset=10&limit=5

            By default a search will return the ids and name of all records matching the condition,
            it may possible that also you want to read other fields name with than name and ids.
            Note: it will always returns id as default field name if field name
            is not given it will return (id and name) otherwise it will return (id and all given fields name).
        """
        result = dict()
        current_user = False
        if post.get('token'):
            current_user = request.env['res.users'].sudo().search(
                [('token', '=', post.get('token'))])
        if not current_user:
            return json.dumps({'error': _('Invalid User Token')})
        try:
            Model = request.env[model].sudo(current_user.id)
        except Exception as e:
            return json.dumps({'error': _('Model Not Found %s' % e)})
        else:
            domain = post.get('domain') and eval(post['domain']) or []
            result = Model.search(domain, offset=int(
                post.get('offset', 0)), limit=post.get('limit') and int(post['limit'] or None),
                                  order=post.get('order') or None).ids
        return json.dumps({'success': result})

    @http.route(['/api/<string:model>/create'
                 ], type='json', auth="public", csrf=False, methods=['POST'])
    def create_data(self, model=None, **post):
        """
            create record , it is medetory to pass model name
            and values for record creation pass as create_vals of JOSN/Dictionary format.
            eg.
            QueryString:
                localhost:8069/api/product.product/create?token=24e635ff9cc74429bed3d420243f5aa6&create_vals={'name':'Apple'}
            Return:
                If record is successfully created then it will return record id eg. {'id':101}
        """
        current_user = False
        if post.get('token'):
            current_user = request.env['res.users'].sudo().search(
                [('token', '=', post.get('token'))])
        if not current_user:
            return json.dumps({'error': _('Invalid User Token')})
        try:
            Model = request.env[model].sudo(current_user.id)
        except Exception as e:
            return json.dumps({'error': _('Model Not Found %s' % e)})
        else:
            if post.get('create_vals'):
                create_vals = post.get('create_vals')
                try:
                    record = Model.create(create_vals)
                except Exception as e:
                    return json.dumps({'error': _(' %s' % e)})
                if record:
                    res = {'success': {'id': record.id}}
                    return json.dumps(res)
            else:
                return json.dumps({'error': _('create_vals not found in query string')})

    @http.route(['/api/<string:model>/update', '/api/<string:model>/update/<int:id>'
                 ], type='json', auth="public", csrf=False, methods=['POST'])
    def update_data(self, model=None, id=None, **post):
        """
            update record , it is medetory to pass model name and record id
            and values for record update pass as update_vals in JOSN/Dictionary format.
            eg.
            QueryString:
                localhost:8069/api/product.product/update/101?token=24e635ff9cc74429bed3d420243f5aa6&update_vals={'name':'Mango'}
            Return:
                If record is successfully updated then it will return {'success':'Record Updated Successfully'}
        """
        current_user = False
        if post.get('token'):
            current_user = request.env['res.users'].sudo().search(
                [('token', '=', post.get('token'))])
        if not current_user:
            return json.dumps({'error': _('Invalid User Token')})
        try:
            Model = request.env[model].sudo(current_user.id)
        except Exception as e:
            return json.dumps({'error': _('Model Not Found %s' % e)})
        else:
            if id:
                if post.get('update_vals'):
                    try:
                        record = Model.browse(id)
                        update_vals = post.get('update_vals')
                        result = record.write(update_vals)
                        if result:
                            return json.dumps({'success': _('Record Updated Successfully')})
                    except Exception as e:
                        return json.dumps({'error': _('Model Not Found %s' % e)})
                else:
                    return json.dumps({'error': _('update_vals not fount in query string')})
            else:
                return json.dumps({'error': _('id not fount in query string')})

    @http.route(['/api/<string:model>/unlink/', '/api/<string:model>/unlink/<int:id>'
                 ], type='http', auth="public", csrf=False)
    def unlink_data(self, model=None, id=None, **post):
        """
            Delete record , it is medetory to pass model name and record id
            For Delete multiple records pass record ids in url parameter as 'unlink_ids' as in list format.
            eg.
            QueryString for Delete single record:
                localhost:8069/api/product.product/unlink/59?token=24e635ff9cc74429bed3d420243f5aa6
            Return:
                If record is successfully deleted then it will return {'success':'Records Successfully Deleted 59'}

            QueryString for Delete multiple records:
                localhost:8069/api/product.product/unlink/?token=24e635ff9cc74429bed3d420243f5aa6&unlink_ids=[60,61]
            Return:
                If record is successfully deleted then it will return {'success':'Records Successfully Deleted [60,61]'}

        """
        current_user = False
        if post.get('token'):
            current_user = request.env['res.users'].sudo().search(
                [('token', '=', post.get('token'))])
        if not current_user:
            return json.dumps({'error': _('Invalid User Token %s'.format(post.get('token')))})
        try:
            Model = request.env[model].sudo(current_user.id)
        except Exception as e:
            return json.dumps({'error': _('Model Not Found %s' % e)})
        else:
            if id:
                try:
                    if Model.browse(id).unlink():
                        return json.dumps({'success': _('Records Successfully Deleted ID - %d' % id)})
                except Exception as e:
                    return json.dumps({'error': _('Model Not Found %s' % e)})
            else:
                try:
                    ids_list = post.get('unlink_ids') and eval(
                        post['unlink_ids']) or []
                    if Model.browse(ids_list).unlink():
                        return json.dumps({'success': _('Records Successfully Deleted %s' % post['unlink_ids'])})
                except Exception as e:
                    return json.dumps({'error': _(' %s' % e)})

    @http.route(['/api/<string:model>/<int:id>/method/<string:method_name>'
                 ], type='http', auth="public", methods=['GET'])
    def method_call(self, model=None, id=None, method_name=None, **post):
        """
            For calling a method of any model , it is medetory to pass model name, record id and method name
            method call based on odoo8 api standards.
            so no need to pass cr,uid,ids,context as method argument. Other then this argument pass as 'args'=[arg1,arg2] in query string
            eg.
            QueryString for calling a method without argument:
                localhost:8069/api/sale.order/26/method/action_button_confirm/?token=1ec448c54a004165b4c0da976b227260
            Return:
                {"success": "True"}
                It will return dictionary its key 'success' and  and its value will be return as per method calling

            QueryString for calling method with arguments:
                'def get_salenote(self, cr, uid, ids, partner_id, context=None)'
                this method if of sale order for calling this method we need to pass partner_id in args

                localhost:8069/api/sale.order/35/method/get_salenote/?token=1ec448c54a004165b4c0da976b227260&args=[3]

            Return:
                {"success": "sale note"}

            QueryString for calling method with keyword argument
                localhost:8069/api/sale.order/33/method/action_invoice_create/?token=1ec448c54a004165b4c0da976b227260&kwargs={'date_invoice':'2016-09-02'}
            It will return
                {"success": "12"}
        """
        current_user = False
        if post.get('token'):
            current_user = request.env['res.users'].sudo().search(
                [('token', '=', post.get('token'))])
        if not current_user:
            return json.dumps({'error': _('Invalid User Token')})
        try:
            Model = request.env[model].sudo(current_user.id)
        except Exception as e:
            return json.dumps({'error': _('Model Not Found %s' % e)})
        else:
            try:
                record = Model.browse(id)
                args = []
                kwargs = {}
                if 'args' in post.keys():
                    args = eval(post['args'])
                if 'kwargs' in post.keys():
                    kwargs = eval(post['kwargs'])
                result = getattr(record, method_name)(*args, **kwargs)
                return json.dumps({'success': result})
            except Exception as e:
                return json.dumps({'error': _(e)})

    @http.route(['/api/<string:model>/<int:id>/method/<string:method_name>'
                 ], type='json', auth="public", methods=['POST'])
    def method_post_call(self, model=None, id=None, method_name=None, **post):
        """
            For calling a method of any model , it is medetory to pass model name, record id and method name
            method call based on odoo8 api standards.
            so no need to pass cr,uid,ids,context as method argument. Other then this argument pass as 'args'=[arg1,arg2] in query string
            eg.
            QueryString for calling a method without argument:
                localhost:8069/api/sale.order/26/method/action_button_confirm/?token=1ec448c54a004165b4c0da976b227260
            Return:
                {"success": "True"}
                It will return dictionary its key 'success' and  and its value will be return as per method calling

            QueryString for calling method with arguments:
                'def get_salenote(self, cr, uid, ids, partner_id, context=None)'
                this method if of sale order for calling this method we need to pass partner_id in args

                localhost:8069/api/sale.order/35/method/get_salenote/?token=1ec448c54a004165b4c0da976b227260&args=[3]

            Return:
                {"success": "sale note"}

            QueryString for calling method with keyword argument
                localhost:8069/api/sale.order/33/method/action_invoice_create/?token=1ec448c54a004165b4c0da976b227260&kwargs={'date_invoice':'2016-09-02'}
            It will return
                {"success": "12"}
        """
        current_user = False
        if post.get('token'):
            current_user = request.env['res.users'].sudo().search(
                [('token', '=', post.get('token'))])
        if not current_user:
            return json.dumps({'error': _('Invalid User Token')})
        try:
            Model = request.env[model].sudo(current_user.id)
        except Exception as e:
            return json.dumps({'error': _('Model Not Found %s' % e)})
        else:
            try:
                record = Model.browse(id)
                args = []
                kwargs = {}
                if 'args' in post.keys():
                    args = eval(post['args'])
                if 'kwargs' in post.keys():
                    kwargs = post['kwargs']
                result = getattr(record, method_name)(*args, **kwargs)
                return json.dumps({'success': result})
            except Exception as e:
                return json.dumps({'error': _(e)})

    @http.route(['/api/<string:model>/method/<string:method_name>'
                 ], type='http', auth="public")
    def method_call_multi_record(self, model=None, method_name=None, **post):
        """
            For calling a method of any model , it is medetory to pass model name, record id and method name
            method call based on odoo8 api standards.
            so no need to pass cr,uid,ids,context as method argument. Other then this argument pass as 'args'=[arg1,arg2] in query string
            eg.
            QueryString for calling a method without argument:
                localhost:8069/api/sale.order/26/method/action_button_confirm/?token=1ec448c54a004165b4c0da976b227260
            Return:
                {"success": "True"}
                It will return dictionary its key 'success' and  and its value will be return as per method calling

            QueryString for calling method with arguments:
                'def get_salenote(self, cr, uid, ids, partner_id, context=None)'
                this method if of sale order for calling this method we need to pass partner_id in args

                localhost:8069/api/sale.order/35/method/get_salenote/?token=1ec448c54a004165b4c0da976b227260&args=[3]

            Return:
                {"success": "sale note"}

            QueryString for calling method with keyword argument
                localhost:8069/api/sale.order/33/method/action_invoice_create/?token=1ec448c54a004165b4c0da976b227260&kwargs={'date_invoice':'2016-09-02'}
            It will return
                {"success": "12"}
        """
        current_user = False
        if post.get('token'):
            current_user = request.env['res.users'].sudo().search(
                [('token', '=', post.get('token'))])
        if not current_user:
            return json.dumps({'error': _('Invalid User Token')})
        try:
            Model = request.env[model].sudo(current_user.id)
        except Exception as e:
            return json.dumps({'error': _('Model Not Found %s' % e)})
        else:
            try:
                if 'ids' in post.keys():
                    ids = eval(post['ids'])
                record = Model.browse(ids)
                args = []
                kwargs = {}
                if 'args' in post.keys():
                    args = eval(post['args'])
                if 'kwargs' in post.keys():
                    kwargs = eval(post['kwargs'])
                result = getattr(record, method_name)(*args, **kwargs)
                return json.dumps({'success': result})
            except Exception as e:
                return json.dumps({'error': _(e)})

    @http.route(['/api/<string:model>/method/<string:method_name>'
                 ], type='json', auth="public", csrf=False, methods=['POST'])
    def call_method(self, model=None, method_name = None,**post):
        """
            create record , it is medetory to pass model name
            and values for record creation pass as create_vals of JOSN/Dictionary format.
            eg.
            QueryString:
                localhost:8069/api/product.product/create?token=24e635ff9cc74429bed3d420243f5aa6&create_vals={'name':'Apple'}
            Return:
                If record is successfully created then it will return record id eg. {'id':101}
        """
        current_user = False
        if post.get('token'):
            current_user = request.env['res.users'].sudo().search(
                [('token', '=', post.get('token'))])
        if not current_user:
            return json.dumps({'error': 'Invalid User Token'})
        try:
            Model = request.env[model].sudo(current_user.id)
        except Exception as e:
            return json.dumps({'error': _('Model Not Found %s' % e)})
        else:
            try:
                args = []
                kwargs = {}
                if 'kwargs' in post.keys():
                    kwargs = post['kwargs']
                result = getattr(Model, method_name)(*args, **kwargs)
                return json.dumps({'success': result})
            except Exception as e:
                return json.dumps({'error': _(e)})
