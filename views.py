from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Servico,Funcionario,Recursos
from .forms import ContatoForm


class IndexTemplateView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['Recursos'] = Recursos.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request,'E-mail enviado com sucesso')
        return super(IndexTemplateView,self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        form.send_mail()
        messages.error(self.request, 'Erro ao enviar o e-mail')
        return super(IndexTemplateView, self).form_invalid(form, *args, **kwargs)

