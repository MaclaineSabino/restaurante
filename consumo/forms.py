from django import forms
from consumo.models import *
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):
    email = forms.CharField(required=True)
    nome = forms.CharField(required=True)
    senha = forms.CharField(required=True)

    def is_valid(self):
        valida = True
        if not super(RegistrarUsuarioForm,self).is_valid():
            self.informa_erro('todos os campos devem está preenchidos')
            valida=False

        user_exists = User.objects.filter(username=self.cleaned_data['email']).exists()
        if(user_exists):
            self.informa_erro('esse email já está cadastrado')
            valida=False

        return valida

    def informa_erro(self,message):

        errors=self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,forms.utils.ErrorList())

        errors.append(message)

class RegistrarCategoriaForm(forms.Form):
    nome = forms.CharField()


    def is_valid(self):
        valida = True
        if not super(RegistrarCategoriaForm,self).is_valid():
            self.informa_erro('O campo não pode está vazio')
            valida=False

        cat_exists = Categoria.objects.filter(nome=self.data['nome']).exists()

        if(cat_exists):
            self.informa_erro('categoria já existe')
            valida=False


        return valida


    def informa_erro(self,message):

        errors=self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,forms.utils.ErrorList())

        errors.append(message)


class RegistrarProdutoForm(forms.Form):




    categoria = forms.IntegerField()
    nome = forms.CharField()


    def is_valid(self):
        valida = True
        if not super(RegistrarProdutoForm,self).is_valid():
            self.informa_erro('O campo não pode está vazio')
            valida=False

        cat_exists = Produto.objects.filter(nome=self.data['nome']).exists()

        if(cat_exists):
            self.informa_erro('categoria já existe')
            valida=False


        return valida


    def informa_erro(self,message):

        errors=self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,forms.utils.ErrorList())

        errors.append(message)


class RegistrarTipoProdutoForm(forms.Form):




    produto = forms.IntegerField()
    nome = forms.CharField()
    descricao = forms.CharField()
    valor = forms.DecimalField()


    def is_valid(self):
        valida = True
        if not super(RegistrarTipoProdutoForm,self).is_valid():
            self.informa_erro('O campo não pode está vazio')
            valida=False

        cat_exists = Produto.objects.filter(nome=self.data['nome']).exists()

        if(cat_exists):
            self.informa_erro('categoria já existe')
            valida=False


        return valida


    def informa_erro(self,message):

        errors=self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,forms.utils.ErrorList())

        errors.append(message)

class DeletarProdutoForm(forms.Form):

    categoria = forms.IntegerField()

    def is_valid(self):
        valida = True
        if not super(DeletarProdutoForm,self).is_valid():
            self.informa_erro('O campo não pode está vazio')
            valida=False





        return valida


    def informa_erro(self,message):

        errors=self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,forms.utils.ErrorList())

        errors.append(message)





class EditarCategorForm(forms.ModelForm):
   #nome = forms.CharField()
   class Meta:
        model = Categoria

        fields = ('nome',)

   def is_valid(self):
       valida=True
       if not super(EditarCategorForm,self).is_valid():
           self.informa_erro('O campo não pode está vazio')
           valida=False




       return valida


   def informa_erro(self,message):

        errors=self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,forms.utils.ErrorList())

        errors.append(message)

class EditarProdutoForm(forms.ModelForm):
   #nome = forms.CharField()
   class Meta:
        model = Produto

        fields = ('nome','categoria')

   def is_valid(self):
       valida=True
       if not super(EditarProdutoForm,self).is_valid():
           self.informa_erro('O campo não pode está vazio')
           valida=False




       return valida


   def informa_erro(self,message):

        errors=self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,forms.utils.ErrorList())

        errors.append(message)


class EditarTipoProdutoForm(forms.ModelForm):
   #nome = forms.CharField()
   class Meta:
        model = TipoProduto

        fields = ('nome','descricao','valor','produto')

   def is_valid(self):
       valida=True
       if not super(EditarTipoProdutoForm,self).is_valid():
           self.informa_erro('O campo não pode está vazio')
           valida=False




       return valida


   def informa_erro(self,message):

        errors=self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,forms.utils.ErrorList())

        errors.append(message)
