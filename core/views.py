from django.shortcuts import render, redirect
from .models import Cliente, Reserva, PedidoDelivery, Cardapio
from .forms import CadastroClienteForm
from datetime import datetime


def cadastro_cliente(request):
    if request.method == 'POST':
        form = CadastroClienteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            endereco = form.cleaned_data['endereco']

            # Salvar os dados no banco de dados
            cliente = Cliente(nome=nome, email=email, endereco=endereco)
            cliente.save()

            return redirect('home')  # Redireciona para a página inicial após o cadastro
    else:
        form = CadastroClienteForm()

    return render(request, 'cadastro_cliente.html', {'form': form})



def reserva(request):
    clientes = Cliente.objects.all()
    reserva_confirmada = False
    cliente = None
    data = None
    hora = None

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        cliente = Cliente.objects.get(id=cliente_id)
        reserva = Reserva(cliente=cliente, data=data, hora=hora)
        reserva.save()

        reserva_confirmada = True

    return render(request, 'reserva.html', {'clientes': clientes, 'reserva_confirmada': reserva_confirmada, 'cliente': cliente, 'data': data, 'hora': hora if reserva_confirmada else None})


def delivery(request):
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        endereco = Cliente.objects.get(id=cliente_id).endereco
        itens = request.POST.getlist('itens')
        total = 0
        for item_id in itens:
            item = Cardapio.objects.get(id=item_id)
            total += item.preco

        return render(request, 'pedido_delivery.html', {'endereco': endereco, 'total': total})
    else:
        clientes = Cliente.objects.all()
        cardapio = Cardapio.objects.all()
        return render(request, 'delivery.html', {'clientes': clientes, 'cardapio': cardapio})


def confirmar_delivery(request, pedido_id):
    pedido = PedidoDelivery.objects.get(id=pedido_id)

    if request.method == 'POST':
        # Lógica para confirmar a entrega, por exemplo, atualizar o status do pedido
        pedido.confirmado = True
        pedido.save()
        return redirect('home')  # Redireciona para a página inicial após a confirmação

    return render(request, 'confirmar_delivery.html', {'pedido': pedido})


def cardapio(request):
    itens = Cardapio.objects.all()

    return render(request, 'cardapio.html', {'itens': itens})


def home(request):
    return render(request, 'home.html')


def lista_clientes(request):
    clientes = Cliente.objects.all()
    for cliente in clientes:
        print(cliente.nome, cliente.email)
    return render(request, 'lista_clientes.html', {'clientes': clientes})
