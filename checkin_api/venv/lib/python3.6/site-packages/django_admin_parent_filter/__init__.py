#!/usr/bin/env python
from django.contrib.admin import SimpleListFilter
from django.utils.safestring import mark_safe
import public


@public.add
class ParentFilter(SimpleListFilter):
    """django admin Parent filter"""
    model = None
    parent_model = None
    parent_parameter_name = 'parent'
    parameter_name = 'parent'
    top_instance = None
    items = []
    depth = -1
    instance = None

    __readme__ = dict(
        model="queryset model",
        parent_model="filter model",
        parent_parameter_name="parent model parameter_name",
        parameter_name="model parameter_name",
        items="initial items"
    )

    def is_bold(self):
        return self.depth == 0

    def get_prefix(self):
        """return prefix string"""
        if self.depth > 0:
            return ("--" * self.depth) + "&gt; "
        return ""

    def get_infix(self):
        """return object prefix"""
        for key in ["title", "name", "headline"]:
            if getattr(self.instance, key, None):
                return getattr(self.instance, key)
        return str(self.instance)

    def get_postfix(self):
        """return postfix string"""
        return ""

    def get_value(self):
        """return instance string"""
        return self.instance.pk

    def get_verbose_value(self):
        parts = [self.get_prefix(), self.get_infix(), self.get_postfix()]
        value = "".join(filter(None, parts))
        if self.is_bold():
            value = "<b>%s</b>" % value
        return mark_safe(value)

    def get_children(self, parent):
        kwargs = {self.parent_parameter_name: parent}
        return self.parent_model.objects.filter(**kwargs).all()

    def child_lookups(self, parent):
        result = []
        depth = self.depth
        childs = self.get_children(parent)
        for child in childs:
            self.depth = depth + 1
            self.instance = child
            value = self.get_value()
            verbose_value = self.get_verbose_value()
            result.append([value, mark_safe(verbose_value)])
            result += self.child_lookups(child)
        return result

    def lookups(self, request, model_admin):
        top = self.top_instance
        print(top)
        return self.items + self.child_lookups(self.top_instance)

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        if not self.value():
            return self.model.objects.filter(**{self.parameter_name: None})
        parent = self.parent_model.objects.get(pk=self.value())
        return self.model.objects.filter(**{self.parameter_name: parent})
