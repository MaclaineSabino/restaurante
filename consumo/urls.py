"""restaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from consumo import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^mesa/(?P<mesa_id>\d+)$',views.abrirConta,name='conta'),
    url(r'^gerenciarprodutos/$',views.gerenciarProduto, name='gerenciarprodutos'),
    url(r'^gerenciarmesas/$',views.gerenciarMesa, name='gerenciarmesas'),
    url(r'^gerenciarmesas/ad/$',views.acrescentarMesa, name='acrescentarmesa'),
    url(r'^gerenciarmesas/re/$',views.removerMesa, name='removermesa'),

    url(r'^novacategoria/$',views.RegistrarCategoriaView.as_view(),name='novacat'),
    url(r'^gerenciarprodutos/editarcategoria/(?P<pk>\d+)$',views.EditarCategoria,name='editcat'),
    url(r'^gerenciarprodutos/deletarcategoria/(?P<pk>\d+)$',views.DeletarCategoria, name='deletecat'),
    url(r'^gerenciarprodutos/novoproduto/$',views.RegistrarProdutoView.as_view(),name='newprod'),
    url(r'^gerenciarprodutos/editarproduto/(?P<pk>\d+)$',views.EditarProdutoView.as_view(),name='editprod'),
    url(r'^gerenciarprodutos/deletarproduto/(?P<pk>\d+)$',views.DeletarProduto, name='deleteprod'),
    url(r'^gerenciarprodutos/novotipoproduto/$',views.RegistrarTipoProdutoView.as_view(),name='newtp'),
    url(r'^gerenciarprodutos/editartp/(?P<pk>\d+)$',views.EditarTpView.as_view(),name='edittp'),
    url(r'^gerenciarprodutos/deletartp/(?P<pk>\d+)$',views.DeletarTp, name='deletetp'),
    url(r'^mesa/(?P<mesa_id>\d+)/categorias/(?P<pk>\d+)$',views.Categorias, name='categorias'),
    url(r'^mesa/(?P<mesa_id>\d+)/categorias/tipoproduto/(?P<pk>\d+)$',views.TipoProdutos, name='tipoprodutos'),
    url(r'^mesa/(?P<mesa_id>\d+)/categorias/tipoproduto/itemconta/(?P<tpk>\d+)$',views.ItemContaDespesa, name='itemconta'),
    url(r'^mesa/(?P<mesa_id>\d+)/categorias/tipoproduto/(?P<pk>\d+)/itemconta/d/(?P<tpk>\d+)$',views.ItemContaDecrescimo, name='itemdecrescimo'),
    url(r'^mesa/(?P<mesa_id>\d+)/f/$',views.finalizarConta, name='finalizar'),
    url(r'^mesa/(?P<mesa_id>\d+)/tipoproduto/(?P<pk>\d+)$',views.acrescentarTpMesa,name='acresctpmesa')



]
