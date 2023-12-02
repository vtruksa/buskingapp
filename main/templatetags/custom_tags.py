from django import template
from django.utils.safestring import mark_safe

register = template.Library()
@register.filter(is_safe=True)
# render a form with bootstrap 5
def render_bs5(form):
    html = ""
    for f in form:
        try:
            input_type = f.field.widget.input_type
        except:
            input_type = 'ta'
        group = 'form-group'
        cl = 'form-control'        
        checked = ''

        if input_type == 'checkbox': 
            group = 'form-check'
            cl = 'form-check-input'
            if f.value(): checked = 'checked'
        html += '<div class='+group+'><label>'+str(f.label)+'</label>'
        if input_type != 'ta':
            html += '<input type="' + input_type + '" name="'+ f.name +'" class="'+ cl +'" '+ checked +' value="'+f.value()+'">'
        else:
            html += '<textarea rows=4 name="'+f.name+'" class="'+cl+'">'+f.value()+'</textarea>'
        html += '<br><small class="form-text text-muted">'+f.help_text+'</small>'
        html+= '</div>'

    return mark_safe(html)