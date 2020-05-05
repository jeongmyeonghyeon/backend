from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['photo_tag', 'caption']
    list_display_links = ['caption']

    def photo_tag(self, post):
        # return f'<img src={post.photo.url}>' # 이렇게 처리하면, django 보안에 의해 < 가 lgt; 로 변환됨. -> html 태그로 인식안함.
        return mark_safe(f'<img src={post.photo.url} width="80px">') # 보안상 문제가 생길 수 있긴 함. 안전하다고 판단되는 경우에만 사용해야 함.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
