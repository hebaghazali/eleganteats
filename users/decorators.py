from django.shortcuts import redirect

def anonymous_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('menu:menu_list')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
