#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2023/6/1 11:35
# @Author  : liuqiao
# @Email   : LQ65535@163.com
# @File    : views_blog.py
# @desc    : views_blog
# @Software: PyCharm

import traceback

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.safestring import mark_safe


from blog.operate_res_code import OperateResCode
from blog.tools.common import get_current_time
from blog.models import Blog
from blog.models import BlogContent


class BlogApi(APIView):
    """
    method: post: 新建本地编写的博客
    method: put: 保存编辑的博文内容
    """

    def post(self, request):
        res = OperateResCode()

        try:
            if not request.user.is_authenticated:
                raise RuntimeError("user not login, request fail !!!")

            data = request.data
            title = data.get("title", None)
            description = data.get("description", None)
            categories = data.get("categories", None)
            tags = data.get("tags", None)
            content = data.get("content", None)
            if content:
                content = content.replace("../../media", "/media")

            current_time = get_current_time()
            new_blog_content_data = {
                "content": content,
                "create_time": current_time,
                "update_time": current_time,
            }
            content_obj = BlogContent.objects.create(**new_blog_content_data)
            new_blog_data = {
                "title": title,
                "description": description,
                "blog_from": "local",
                "categories": categories,
                "tags": tags,
                "content_id": content_obj.pk,
                "create_time": current_time,
                "update_time": current_time,
            }
            Blog.objects.create(**new_blog_data)

            return Response(res.success)

        except:
            print(traceback.format_exc())
            return Response(res.unknown_error, status=res.unknown_error["code"])

    def put(self, request, blog_pk):
        res = OperateResCode()

        try:
            if not request.user.is_authenticated:
                raise RuntimeError("user not login, request fail !!!")

            data = request.data
            title = data.get("title", None)
            description = data.get("description", None)
            categories = data.get("categories", None)
            tags = data.get("tags", None)
            content = data.get("content", None)
            if content:
                content = content.replace("../../media", "/media")

            current_time = get_current_time()
            new_blog_data = {
                "title": title,
                "description": description,
                "blog_from": "local",
                "categories": categories,
                "tags": tags,
                "update_time": current_time,
            }
            blog_obj = Blog.objects.get(pk=blog_pk)
            if blog_obj.blog_from != "local":
                raise RuntimeError("this method only support local write blog...")
            blog_obj.__dict__.update(**new_blog_data)
            blog_obj.save()

            new_blog_content_data = {
                "content": content,
                "update_time": current_time,
            }
            BlogContent.objects.filter(pk=blog_obj.content_id).update(**new_blog_content_data)

            return Response(res.success)

        except:
            print(traceback.format_exc())
            return Response(res.unknown_error, status=res.unknown_error["code"])
