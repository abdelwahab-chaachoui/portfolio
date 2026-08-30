from django.contrib import admin
from .models import Post, Keyword, Comment
from django.contrib import messages
from django.utils.translation import ngettext

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'status')
    list_filter = ('status', 'keywords')
    search_fields = ('title', 'status')
    actions = ['publish_post', 'unpublish_post']

    # TODO fix this
    @admin.action(description='Publish selected post(s)')
    def publish_post(self, request, queryset):
        """
        Change the Status of the Post to the next one
        at first a post is Created -> then it goes to Draft
        by the end it goes to Published
        """

        current_status = request.post.status
        if current_status == 0 or current_status == 1:
            updated = queryset.update(status=2)
            self.message_user(
                request,
                ngettext(
                    "%d posts was successfully marked as published.",
                    "%d posts were successfully marked as published.",
                    updated,
                )
                % updated,
                messages.SUCCESS,
            )
        else:
            self.message_user(
                request,
                "Selected post(s) are already published.",
                messages.WARNING,
            )

    # TODO fix this
    @admin.action(description='Draft selected post(s)')
    def unpublish_post(self, request, queryset):
        current_status = request.post.status
        if current_status == 2:
            updated = queryset.update(status=1)
            self.message_user(
                request,
                ngettext(
                    "%d posts was successfully marked as drafted.",
                    "%d posts were successfully marked as drafted.",
                    updated,
                )
                % updated,
                messages.SUCCESS,
            )
        else:
            self.message_user(
                request,
                "Selected post(s) cannot be drafted.",
                messages.WARNING,
            )


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'post', 'active')
    list_filter = ('post', 'active', 'date')
    search_fields = ('id', 'post')
    actions = ['approve_comment']

    # TODO fix this
    @admin.action(description='Approve selected Comment(s)')
    def approve_comment(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(
            request,
            ngettext(
                "%d comment was approved.",
                "%d comments were approved.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )