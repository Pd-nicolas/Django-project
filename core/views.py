from django.shortcuts import render, redirect
from .models import Cliente, Reserva, PedidoDelivery, Cardapio
from .forms import CadastroClienteForm

def cadastro_cliente(request):
    if request.method == 'POST':
        form = CadastroClienteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']

            # Salvar os dados no banco de dados
            cliente = Cliente(nome=nome, email=email)
            cliente.save()

            return redirect('home')  # Redireciona para a página inicial após o cadastro
    else:
        form = CadastroClienteForm()

    return render(request, 'cadastro_cliente.html', {'form': form})


def reserva(request):
    clientes = Cliente.objects.all()
    return render(request, 'reserva.html', {'clientes': clientes})


def delivery(request):
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        endereco = request.POST['endereco']
        itens = request.POST['itens']
        cliente = Cliente.objects.get(id=cliente_id)
        pedido = PedidoDelivery(cliente=cliente, endereco=endereco, itens=itens)
        pedido.save()
        return redirect('home')  # Redireciona para a página inicial após o pedido de delivery
    else:
        clientes = Cliente.objects.all()
        return render(request, 'delivery.html', {'clientes': clientes})

def confirmar_delivery(request, pedido_id):
    pedido = PedidoDelivery.objects.get(id=pedido_id)

    if request.method == 'POST':
        # Lógica para confirmar a entrega, por exemplo, atualizar o status do pedido
        pedido.confirmado = True
        pedido.save()
        return redirect('home')  # Redireciona para a página inicial após a confirmação

    return render(request, 'confirmar_delivery.html', {'pedido': pedido})



def cardapio(request):
    # Obtenha todos os itens do cardápio do banco de dados
    itens = Cardapio.objects.all()

    return render(request, 'cardapio.html', {'itens': itens})


def home(request):
    return render(request, 'home.html')


def lista_clientes(request):
    clientes = Cliente.objects.all()
    for cliente in clientes:
        print(cliente.nome, cliente.email)
    return render(request, 'lista_clientes.html', {'clientes': clientes})

