
var categorialis=[];
var prodlista=[];
var tipoprodulis=[];
var tip=null;
var arrayLinks =[];
var arrayMesaLinks=[]; 

function percentual(votos,soma){
	var resultado=(votos/soma)*100;
	
	return document.write(resultado+"%");
}
function ConfirmarAlteracao(){		
if (confirm ("Deseja realmente realizar essa ação?")){
	
	return true;
}	
		
	
else{		
	
return false;
}

}

function refreshPag(){
	
if( window.localStorage )
{
if( !localStorage.getItem( 'firstLoad' ) )
{
localStorage[ 'firstLoad' ] = true;
window.location.reload();
}
else
localStorage.removeItem( 'firstLoad' );
}
}

function listaCategorias(lista){
	
	for(var i=0;i<lista.length;i++){
		
		var nome = lista[i][1];
		$('#painel_categorias').append('<li role="presentation" class="active btnprod"><a>'+nome+'</a></li>');
		
	}
	
}

function pegaIdCategoria(nome){
	var a=null;
	for(var i=0;i<categorialis.length;i++){
		if(nome == categorialis[i][1]){
			a = categorialis[i][0];
		}
	}
	
	return a;
}
function searchSubprodutos(){
	$('#painel_produtos .btnsubprod').click(function(e){
	var valor = $(this).text();
	
	var id = pegaIdProduto(valor);
	
	listaSubProdutos(id);
	
	
});
}
function geralink(caminho,tp){
	var link = '/mesa/'+caminho+'/tipoproduto/'+tp;
	
	return link;
}

function pegaLinksMesa(){
	for(var i=0;i<arrayLinks.length;i++){
		
		arrayMesaLinks[i]=$(".link_modal").eq(i).attr("href");
		var text = arrayMesaLinks[i];
		var text2 = text.substring(0,text.length-1);
		arrayMesaLinks[i]=text2;
		
		
	
		
		
	}
}

function getLinkModal(id){

	
	
	for(var i=0;i<arrayMesaLinks.length;i++){
				
		$(".link_modal").eq(i).attr("href",arrayMesaLinks[i]+id);
	}
	
	
}
	
function listarDadosTp(nome){
	
	for(var i=0;i<tipoprodulis.length;i++){
		if(nome == tipoprodulis[i][1]){
			tip=tipoprodulis[i][0];
			$('#myModalLabel').text(tipoprodulis[i][1]);
			$('#descricao').text(tipoprodulis[i][2]);
			$('#prec').text(tipoprodulis[i][3]);
		    getLinkModal(tipoprodulis[i][0]);
		}
	}
	
}

function getNomeTp(){
		
	$('.btnnomes').click(function(e){
		
		var valor = $(this).text();
		
		listarDadosTp(valor);
		
	});
}
function listaProdutos(id_categoria){
	$("#painel_subprodutos").html('');
		$('#painel_produtos').html('');
		for(var i=0;i<prodlista.length;i++){
			if(id_categoria == prodlista[i][2]){
				
				$('#painel_produtos').append('<li role="presentation" class="active btnsubprod"><a>'+prodlista[i][1]+'</a></li>');
			}
			
			
		}
		
	searchSubprodutos();
}
function pegaIdProduto(nome){
	var b=null;
	for(var i=0;i<prodlista.length;i++){
		if(nome == prodlista[i][1]){
			b=prodlista[i][0];
		}
	}
	return b;
}

function listaSubProdutos(id_produto){
	$("#painel_subprodutos").html('');
	for(var i=0;i<tipoprodulis.length;i++){
		if(id_produto == tipoprodulis[i][4]){
			$('#painel_subprodutos').append('<button type="button" class="btn btn-primary btn-lg btnnomes" data-toggle="modal" data-target="#myModal">'
  					+tipoprodulis[i][1]+
			'</button>');
			
		}
	}
	getNomeTp();
}


function valorSelect(){
	var items = document.getElementById('categoria');
	var items2 = document.getElementById('produto');
	var items3 = document.getElementById('tipoproduto');
	$("#linkedit").html('<a href="/gerenciarprodutos/editarcategoria/'+items.value+'">editar</a>'); 
    $("#linkdelete").html('<a href="/gerenciarprodutos/deletarcategoria/'+items.value+'">excluir</a>');
	$("#editprod").html('<a href="/gerenciarprodutos/editarproduto/'+items2.value+'">editar</a>');
	$("#proddelete").html('<a href="/gerenciarprodutos/deletarproduto/'+items2.value+'">excluir</a>');
	$("#tpedit").html('<a href="/gerenciarprodutos/editartp/'+items3.value+'">editar</a>'); 
    $("#tpdelete").html('<a href="/gerenciarprodutos/deletartp/'+items3.value+'">excluir</a>');  

items.addEventListener('change', function(){
    
    $("#linkedit").html('<a href="/gerenciarprodutos/editarcategoria/'+this.value+'">editar</a>'); 
    $("#linkdelete").html('<a href="/gerenciarprodutos/deletarcategoria/'+this.value+'">excluir</a>'); 
});


items2.addEventListener('change', function(){
    
    $("#editprod").html('<a href="/gerenciarprodutos/editarproduto/'+this.value+'">editar</a>'); 
    $("#proddelete").html('<a href="/gerenciarprodutos/deletarproduto/'+this.value+'">excluir</a>'); 
});


items3.addEventListener('change', function(){
    
    $("#tpedit").html('<a href="/gerenciarprodutos/editartp/'+this.value+'">editar</a>'); 
    $("#tpdelete").html('<a href="/gerenciarprodutos/deletartp/'+this.value+'">excluir</a>'); 
});
	
	
	
}

function converter(id){

	var campo = document.getElementById(id);
	
	campo.value = campo.value.replace(',','.');
	
	
}

function adicionarClasse(){
	$(".active").click(function(e){
		
		$(this).addClass("clicado");
		
		
	});
}


function randOrd() {

return (Math.round(Math.random())-0.5);

}



function selecionarMesa(){
	
	$('#btn_sorteio').click(function(e){
		$(".sorteada").empty();
		$(".mesasr").css("background-color","#FF4500");
		$(".mesasr").css("border","10px solid");
		

	var mesas = $(".mesasr");
	
	for(i=0; i<mesas.length; i++){
		mesas.eq(i).animate(
			{opacity:0.3}
			,1000);
			
			mesas.eq(i).animate(
			{opacity:1.0}
			,1500);
		
		//mesas.eq(i).removeClass('escolha').slow();
	}
	mesas.sort(randOrd);
	mesas.eq(4).css("background-color","white").append('<span class="sorteada">sorteada</span>');
	mesas.eq(4).css("border","10px solid #000080");
	
	
});
}


$(document).ready(function(e){

	
	
$(".active").click(function(e){
		
		$(this).addClass("clicado");
		
		
	});
	    
 $('#finalizarfatur').click(function(e){
			
	window.location.href = "../1";
	//var a = window.location.replace("../");
	  
   // $('#btn_inicio').trigger('click');

			
		});
		
		
$('.btnprod').click(function(e){
   var valor = $(this).text();			
  var id =  pegaIdCategoria(valor);

			listaProdutos(id);
		});
		
		
	
		
		
$('#btnpdf').click(function() {
	now = new Date
	var dia     = now.getDate();
	var mes     = now.getMonth();
	var ano    = now.getFullYear(); 
	var hora = now.getHours();
	var min = now.getMinutes();
	var str_data = dia + '.' + (mes+1) + '.' + ano+'-'+hora+'h'+min+'min' ;
	
  var doc = new jsPDF('landscape', 'pt', 'a4');
  
  doc.addHTML($('#gerapdf'), function() {
    doc.save(str_data+".pdf");
  });
});		
		
		
		
		
		arrayLinks = $(".link_modal");
		
		pegaLinksMesa();
		
		
	
		
		
		
		
		
	valorSelect();
   
   //-------------------------------------
    
    
 
  

   
});



