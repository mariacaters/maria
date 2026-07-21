from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(
        request,
        "home.html",
        {
            "orders": MenuOrder.objects.prefetch_related(
                "details",
                "sections"
            ).order_by("-id"),

            "bills": Bill.objects.prefetch_related(
                "details",
                "items"
            ).order_by("-id"),
        },
    )



@login_required
def new_order(request):
    if request.method == "POST":
        order = MenuOrder.objects.create()

        keys = request.POST.getlist("detail_key[]")
        values = request.POST.getlist("detail_value[]")

        for key, value in zip(keys, values):
            if key.strip() or value.strip():
                OrderDetail.objects.create(
                    order=order,
                    key=key,
                    value=value
                )
        categories = request.POST.getlist("category[]")
        items = request.POST.getlist("items[]")
        for category, item in zip(categories, items):
            if category.strip():
                MenuSection.objects.create(
                    menu_order=order,
                    category=category,
                    items=item
                )
        return redirect("home")
    return render(request, "new_order.html")



@login_required
def edit_order(request, order_id):
    order = get_object_or_404(MenuOrder, id=order_id)
    if request.method == "POST":
        MenuSection.objects.filter(menu_order=order).delete()
        OrderDetail.objects.filter(order=order).delete()

        keys = request.POST.getlist("detail_key[]")
        values = request.POST.getlist("detail_value[]")

        for key, value in zip(keys, values):
            if key.strip() or value.strip():
                OrderDetail.objects.create(
                    order=order,
                    key=key,
                    value=value
                )
        MenuSection.objects.filter(menu_order=order).delete()
        categories = request.POST.getlist("category[]")
        items = request.POST.getlist("items[]")
        for category, item in zip(categories, items):
            if category.strip():
                MenuSection.objects.create(
                    menu_order=order,
                    category=category,
                    items=item
                )
        return redirect("home")
    sections = MenuSection.objects.filter(menu_order=order)
    return render(
        request,
        "edit_order.html",
        {
            "order": order,
            "sections": sections,
        }
    )


@login_required
def delete_order(request, order_id):
    order = get_object_or_404(MenuOrder, id=order_id)
    order.delete()
    return redirect("home")


@login_required
def download_pdf(request, pk):
    from weasyprint import HTML
    order = MenuOrder.objects.get(pk=pk)

    html = render_to_string(
        "menu_pdf.html",
        {
            "order": order,
        },
        request=request,
    )

    pdf = HTML(
        string=html,
        base_url=request.build_absolute_uri("/")
    ).write_pdf()

    return HttpResponse(
        pdf,
        content_type="application/pdf",
        headers={
            "Content-Disposition": f'inline; filename="menu_{order.id}.pdf"'
        },
    )

@login_required
def new_bill(request):
    if request.method == "POST":

        bill = Bill.objects.create(
            total=request.POST.get("total", "")
        )

        keys = request.POST.getlist("detail_key[]")
        values = request.POST.getlist("detail_value[]")

        for key, value in zip(keys, values):
            BillDetail.objects.create(
                bill=bill,
                key=key,
                value=value
            )

        item_keys = request.POST.getlist("item_key[]")
        item_values = request.POST.getlist("item_value[]")

        for key, value in zip(item_keys, item_values):
            BillItem.objects.create(
                bill=bill,
                key=key,
                value=value
            )

        return redirect("home")

    return render(request, "new_bill.html")

@login_required
def edit_bill(request, id):
    bill = get_object_or_404(Bill, id=id)

    if request.method == "POST":

        bill.total = request.POST.get("total", "")
        bill.save()

        BillDetail.objects.filter(bill=bill).delete()
        BillItem.objects.filter(bill=bill).delete()

        keys = request.POST.getlist("detail_key[]")
        values = request.POST.getlist("detail_value[]")

        for key, value in zip(keys, values):
            if key.strip() or value.strip():
                BillDetail.objects.create(
                    bill=bill,
                    key=key,
                    value=value
                )

        item_keys = request.POST.getlist("item_key[]")
        item_values = request.POST.getlist("item_value[]")

        for key, value in zip(item_keys, item_values):
            if key.strip() or value.strip():
                BillItem.objects.create(
                    bill=bill,
                    key=key,
                    value=value
                )

        return redirect("home")

    return render(
        request,
        "edit_bill.html",
        {
            "bill": bill
        }
    )

@login_required
def delete_bill(request, id):
    bill = get_object_or_404(Bill, id=id)

    bill.delete()

    return redirect("home")

@login_required
def print_bill(request, id):
    try:
        from weasyprint import HTML
    except Exception as e:
        return HttpResponse(f"<pre>{repr(e)}</pre>", status=500)

    bill = get_object_or_404(
        Bill.objects.prefetch_related("details", "items"),
        id=id
    )

    html_string = render_to_string(
        "bill_pdf.html",
        {
            "bill": bill,
        }
    )

    pdf = HTML(
        string=html_string,
        base_url=request.build_absolute_uri("/")
    ).write_pdf()

    response = HttpResponse(
        pdf,
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        f'inline; filename="Bill-{bill.id}.pdf"'
    )

    return response
