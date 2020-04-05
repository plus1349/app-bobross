from rest_framework.renderers import JSONRenderer as BaseJSONRenderer


class JSONRenderer(BaseJSONRenderer):
    def get_indent(self, accepted_media_type, renderer_context):
        return 2
