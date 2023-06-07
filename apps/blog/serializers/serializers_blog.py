#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2023/6/1 19:49
# @Author  : liuqiao
# @Email   : LQ65535@163.com
# @File    : serializers_blog.py
# @desc    : serializers_blog
# @Software: PyCharm

import datetime
import time
from rest_framework import serializers
from ..models import Blog


class BlogSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()  # 分类名称
    tags_name = serializers.SerializerMethodField()  # 标签名称

    def get_category_name(self, obj):
        return obj.category_name()

    def get_tags_name(self, obj):
        return obj.tags_name()

    class Meta:
        model = Blog
        fields = '__all__'
        # exclude = ["id", ]

