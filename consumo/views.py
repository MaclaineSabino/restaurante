from django.shortcuts import render,get_object_or_404,redirect,render_to_response
from django.template import RequestContext
from consumo.models import *
from django.views.generic.base import View
from consumo.forms import *
from django.db.models.functions import Lower
import json
from django.core.serializers.json import DjangoJSONEncoder
import decimal
# Create your views here.

def index(request):
    categoria = Categoria.objects.all().order_by(Lower('nome')).values_list()
    catejson = json.dumps(list(categoria),cls=DjangoJSONEncoder)

    produt = Produto.objects.all().order_by(Lower('nome')).values_list()
    produtjson = json.dumps(list(produt),cls=DjangoJSONEncoder)

    tipoproduto = TipoProduto.objects.all().order_by(Lower('nome')).values_list()
    tipoprodjson = json.dumps(list(tipoproduto),cls=DjangoJSONEncoder)

    return render(request,'index.html',{


        'mesas':Mesa.objects.all(),
        'categ':catejson,
        'produ':produtjson,
        'tipoprod':tipoprodjson
    })


def abrirConta(request,mesa_id):
    mesa = Mesa.objects.get(id=mesa_id)
    conta=mesa.Conta()
    itemconta = ItemConta.objects.filter(conta=conta)
    tipoproduto2 = TipoProduto.objects.all().order_by(Lower('nome'))

    categoria = Categoria.objects.all().order_by(Lower('nome')).values_list()
    catejson = json.dumps(list(categoria),cls=DjangoJSONEncoder)

    produt = Produto.objects.all().order_by(Lower('nome')).values_list()
    produtjson = json.dumps(list(produt),cls=DjangoJSONEncoder)

    tipoproduto = TipoProduto.objects.all().order_by(Lower('nome')).values_list()
    tipoprodjson = json.dumps(list(tipoproduto),cls=DjangoJSONEncoder)





    return render(request,'contas.html',{
        'mesas':Mesa.objects.all(),
        'cont':conta,
        'tp':tipoproduto2,
        'item':itemconta,
        'categ':catejson,
        'produ':produtjson,
        'tipoprod':tipoprodjson
    })


def gerenciarProduto(request):



    return render(request,'gerenciarprodutos.html',{
        'categorias':Categoria.objects.all().order_by(Lower('nome')),
        'produtos':Produto.objects.all().order_by(Lower('nome')),
        'tipo_produtos':TipoProduto.objects.all().order_by(Lower('nome'))
    })



class RegistrarCategoriaView(View):
    template='newcat.html'

    def get(self,request):
        return render(request,self.template)

    def post(self,request):
        form = RegistrarCategoriaForm(request.POST)
        if form.is_valid():
            dados_form = form.cleaned_data
            cat_nome = Categoria(nome=dados_form['nome'])
            cat_nome.save()
            return redirect('gerenciarprodutos')
        return render(request,self.template,{'form':form})

class RegistrarProdutoView(View):
    template = 'novoprod.html'


    def get(self,request):
        catego = Categoria.objects.all()
        return render(request,self.template,{'catego':catego})

    def post(self,request):
        catego = Categoria.objects.all()

        form = RegistrarProdutoForm(request.POST)

        if form.is_valid():
            dados_form = form.cleaned_data
            cat = Categoria.objects.get(id=dados_form['categoria'])
            prod = Produto(nome=dados_form['nome'],
                           categoria=cat)

            prod.save()
            return redirect('gerenciarprodutos')
        return render(request,self.template,{'form':form,
                                             'catego':catego})

class RegistrarTipoProdutoView(View):
    template = 'novotp.html'


    def get(self,request):
        tp = Produto.objects.all()
        return render(request,self.template,{'tp':tp})

    def post(self,request):
        tp = Produto.objects.all()

        form = RegistrarTipoProdutoForm(request.POST)

        if form.is_valid():
            dados_form = form.cleaned_data
            prod = Produto.objects.get(id=dados_form['produto'])
            tprod = TipoProduto(nome=dados_form['nome'],
                           descricao=dados_form['descricao'],
                           valor = dados_form['valor'],
                           produto=prod)

            tprod.save()
            return redirect('gerenciarprodutos')
        return render(request,self.template,{'form':form,
                                             'tp':tp})

def EditarCategoria(request,pk):
    template = 'editcat.html'
    categ = get_object_or_404(Categoria,pk=pk)

    if request.method=="POST":
        form = EditarCategorForm(request.POST,instance=categ)
        if form.is_valid:
            form.save()
        return gerenciarProduto(request)
    else:
        form = EditarCategorForm(request.POST,instance=categ)




    return render(request,template ,{'form':form,
                                           'categ':categ})

def DeletarCategoria(request,pk):
    categ = Categoria.objects.get(id=pk)
    categ.delete()
    return gerenciarProduto(request)


class EditarProdutoView(View):
    template = 'editprod.html'
    catego = Categoria.objects.all()

    def get(self,request,pk):
        produto = get_object_or_404(Produto,pk=pk)
        catego = Categoria.objects.all()
        return render(request,self.template,{'categ':catego,
                                             'produto':produto})

    def post(self,request,pk):
        produto = get_object_or_404(Produto,pk=pk)
        catego = Categoria.objects.all()

        form = RegistrarProdutoForm(request.POST)

        if form.is_valid():
            dados_form = form.cleaned_data
            cat = Categoria.objects.get(id=dados_form['categoria'])
            #prod = Produto(nome=dados_form['nome'],
                           #categoria=cat)
            produto.nome=dados_form['nome']
            produto.categoria=cat

            produto.save()
            return redirect('gerenciarprodutos')
        return render(request,self.template,{'form':form,
                                             'categ':catego,
                                             'produto':produto})

def DeletarProduto(request,pk):



    prod = Produto.objects.get(id=pk)
    prod.delete()
    return redirect('gerenciarprodutos')


class EditarTpView(View):
    template = 'edittp.html'

    def get(self,request,pk):
        prod = Produto.objects.all()
        tipoproduto = TipoProduto.objects.get(id=pk)
        return render(request,self.template,{'prod':prod,
                                             'tipoproduto':tipoproduto})

    def post(self,request,pk):
        prod = Produto.objects.all()
        tipoproduto=get_object_or_404(TipoProduto,pk=pk)

        form = RegistrarTipoProdutoForm(request.POST)

        if form.is_valid():
            dados_form = form.cleaned_data
            prod = Produto.objects.get(id=dados_form['produto'])
            tipoproduto.nome=dados_form['nome']
            tipoproduto.descricao=dados_form['descricao']
            tipoproduto.valor=dados_form['valor']
            tipoproduto.produto=prod
            tipoproduto.save()



            return redirect('gerenciarprodutos')
        return render(request,self.template,{'form':form,
                                             'pro':prod,
                                             'tipoproduto':tipoproduto})

def DeletarTp(request,pk):
    tp = TipoProduto.objects.get(id=pk)
    tp.delete()
    return redirect('gerenciarprodutos')


def Categorias(request,mesa_id,pk):
    template='itemproduto.html'

    mesa = Mesa.objects.get(id=mesa_id)
    conta=mesa.Conta()
    itemconta = ItemConta.objects.filter(conta=conta)
    categoria = Categoria.objects.get(id=pk)
    produtos = Produto.objects.filter(categoria=categoria)

    return render(request,template,{'produt':produtos,
                                    'cont':conta,
                                    'categorias':Categoria.objects.all(),
                                    'item':itemconta})

def TipoProdutos(request,mesa_id,pk):
    template = 'itemtipoproduto.html'
    mesa = Mesa.objects.get(id=mesa_id)
    conta=mesa.Conta()
    itemconta = ItemConta.objects.filter(conta=conta)
    produto = Produto.objects.get(id=pk)
    produtos = Produto.objects.filter(categoria=produto.categoria)

    tp = TipoProduto.objects.filter(produto=produto)

    return render(request,template,{'tp':tp,
                                    'produto':produto,
                                    'produt':produtos,
                                    'cont':conta,
                                    'categorias':Categoria.objects.all(),
                                    'item':itemconta})


def ItemContaDespesa(request,mesa_id,tpk):

    mesa = Mesa.objects.get(id=mesa_id)
    conta=mesa.Conta()
    conta.ocuparMesa()
    tipoprd = TipoProduto.objects.get(id=tpk)
    item_conta,resultado=ItemConta.objects.get_or_create(conta=conta,tipo_produto=tipoprd)

    item_conta.quantidade=item_conta.quantidade+1
    item_conta.parcial = tipoprd.valor*item_conta.quantidade
    item_conta.save()
    item_conta.despesaConta()
    return redirect('conta',mesa_id)

def ItemContaDecrescimo(request,mesa_id,pk,tpk):
    mesa = Mesa.objects.get(id=mesa_id)
    conta=mesa.Conta()
    tipoprd = TipoProduto.objects.get(id=tpk)
    ic = ItemConta.objects.get(id=pk)
    if ic.quantidade >= 1:
        ic.quantidade = ic.quantidade - 1
        ic.parcial = tipoprd.valor*ic.quantidade
        ic.save()
        conta.valor_total=conta.valor_total-tipoprd.valor
        conta.save()
    if ic.quantidade == 0:
        ic.delete()
        conta.desocuparMesa()
    return redirect('conta',mesa_id)

def gerenciarMesa(request):
    return render(request,'gerenciarmesas.html',{
        'mesas':Mesa.objects.all()})

def acrescentarMesa(request):
    qtd = Mesa.objects.all()
    valor = len(qtd)+1
    texto = 'mesa0'+str(valor)

    mesa = Mesa(nome=texto)
    mesa.save()
    return redirect('gerenciarmesas')

def removerMesa(request):
    qtd = Mesa.objects.all()
    qtd[len(qtd)-1].delete()

    return redirect('gerenciarmesas')



def finalizarConta(request,mesa_id):
    template='nota.html'
    mesa = Mesa.objects.get(id=mesa_id)
    conta=mesa.Conta()
    ic = ItemConta.objects.filter(conta=conta)
    if ic != None:
        conta.finalizarConta()
        return render(request,template,{
        'iconta':ic,
        'conta':conta,
        'mesa':mesa
             })
    return redirect('index')

def acrescentarTpMesa(request,mesa_id,pk):
    mesa = Mesa.objects.get(id=mesa_id)
    conta=mesa.Conta()
    conta.ocuparMesa()
    tipoprd = TipoProduto.objects.get(id=pk)
    item_conta,resultado=ItemConta.objects.get_or_create(conta=conta,tipo_produto=tipoprd)

    item_conta.quantidade=item_conta.quantidade+1
    item_conta.parcial =tipoprd.valor*decimal.Decimal(item_conta.quantidade)
    item_conta.save()
    item_conta.despesaConta()
    #conta.valor_total= conta.valor_total+tipoprd.valor
    #conta.save()

    return redirect('conta',mesa_id)
