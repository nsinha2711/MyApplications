from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pagination(request, data, num=10):
    paginator = Paginator(data, num)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except Exception as EmptyPage:
        items = paginator.page(paginator.num_pages)
    index = items.number - 1
    max_index = len(paginator.page(paginator.num_pages))
    start_index = index - 5 if index >=5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    items = paginator.page(paginator.num_pages)
    context = {
        "items": items,
        "page_range": page_range
    }
    return items, page_range
