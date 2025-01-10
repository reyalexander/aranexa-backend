from rest_framework import viewsets
from .models import *
from .serializers import UserSerializer, AccountSerializer, AccountSummarySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# summary/views.py (continuación)
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO

from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

@api_view(["GET"])
def summary_view(request):
    """
    Retorna toda la información (Account + related models) 
    en formato JSON, usando el serializer definido.
    Se espera ?account_id=123 en el query param.
    """
    account_id = request.query_params.get("account_id")
    if not account_id:
        return Response({"error": "account_id is required"}, status=400)

    account = get_object_or_404(Account, pk=account_id)
    serializer = AccountSummarySerializer(account)
    return Response(serializer.data, status=200)


def summary_pdf_view(request):
    """Genera un PDF usando xhtml2pdf."""
    account_id = request.GET.get("account_id")
    if not account_id:
        return HttpResponse("No account_id provided", status=400)
    
    account = get_object_or_404(Account, pk=account_id)
    
    # Obtén datos de otros modelos relacionados, si aplica
    # Por ejemplo:
    # company_info = CompanyInformation.objects.filter(account_id=account_id)
    # brand_info = CompanyBrand.objects.filter(account_id=account_id)
    # etc.

    context = {
        "account": account,
        # "company_info": company_info,
        # "brand_info": brand_info,
        # ...
    }

    # 1. Generamos el HTML a partir de una plantilla
    html_string = render_to_string("summary_pdf.html", context)

    # 2. Convertimos el HTML a PDF con xhtml2pdf
    pdf_buffer = BytesIO()
    pisa_status = pisa.CreatePDF(
        src=html_string,           # cadena de HTML
        dest=pdf_buffer,           # salida en buffer
        encoding='utf-8'
    )

    if pisa_status.err:
        return HttpResponse("Error al generar PDF", status=500)

    # 3. Retornar el PDF como respuesta
    pdf_buffer.seek(0)
    response = HttpResponse(content_type="application/pdf")
    filename = f"summary_{account_id}.pdf"
    response["Content-Disposition"] = f'inline; filename="{filename}"'
    response.write(pdf_buffer.read())

    return response

