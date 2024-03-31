from django.shortcuts import redirect


class StoreSlugMixin:
    def dispatch(self, request, *args, **kwargs):
        store_slug = request.session.get('store_slug', None)

        if not store_slug:
            return redirect('home:intro')

        return super().dispatch(request, *args, **kwargs)
