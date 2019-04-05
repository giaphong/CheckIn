#!/usr/bin/env python
# -*- coding: utf-8 -*-
import public
import applescript


@public.add
def playing():
    """return vk.com page url if audio is playing"""
    return applescript.tell.app("Google Chrome", """
repeat with w in every window
    repeat with t in every tab of w
        if "https://vk.com/" is in (get URL of t) then
            tell t to set is_playing to execute javascript "!!Array.prototype.find.call(document.querySelectorAll('.audio_playing'),function(elem){return true;})"
            if (is_playing) then return (get URL of t) --vk allows only 1 playing tab
        end if
    end repeat
end repeat
""").out


@public.add
def pause():
    """pause vk.com audio"""
    applescript.tell.app("Google Chrome", """
repeat with w in every window
    repeat with t in every tab of w
        if "https://vk.com/" is in (get URL of t) then
            tell t to set is_playing to execute javascript "!!Array.prototype.find.call(document.querySelectorAll('.audio_playing'),function(elem){return true;})"
            if (is_playing) then
                tell t to execute javascript "!!Array.prototype.find.call(document.querySelectorAll('.audio_page_player_play'),function(elem){elem.click();})"
            end if
        end if
    end repeat
end repeat
""")


@public.add
def play():
    """continue play vk.com audio and return vk page url"""
    return applescript.tell.app("Google Chrome", """
repeat with w in every window
    repeat with t in every tab of w
        if "https://vk.com/" is in (get URL of t) then
            tell t to set is_playing to execute javascript "!!Array.prototype.find.call(document.querySelectorAll('.audio_playing'),function(elem){return true;})"
            if (not is_playing) then
                tell t to execute javascript "!!Array.prototype.find.call(document.querySelectorAll('.audio_page_player_play'),function(elem){elem.click();})"
                return (get URL of t)
            end if
        end if
    end repeat
end repeat
""").out
