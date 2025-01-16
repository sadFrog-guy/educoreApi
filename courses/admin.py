from datetime import timedelta

from django import forms
from django.contrib import admin
from .models import Course

class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    # Добавляем поля для ввода числового значения и единицы измерения
    duration_value = forms.IntegerField(label="Продолжительность (число)")
    duration_unit = forms.ChoiceField(
        label="Единица измерения",
        choices=[('days', 'Дни'), ('weeks', 'Недели'), ('months', 'Месяцы')],
        initial='days'
    )

    def clean(self):
        cleaned_data = super().clean()
        duration_value = cleaned_data.get('duration_value')
        duration_unit = cleaned_data.get('duration_unit')

        # Если поле duration_value и duration_unit присутствуют, вычисляем timedelta
        if duration_value and duration_unit:
            if duration_unit == 'days':
                cleaned_data['duration'] = timedelta(days=duration_value)
            elif duration_unit == 'weeks':
                cleaned_data['duration'] = timedelta(weeks=duration_value)
            elif duration_unit == 'months':
                cleaned_data['duration'] = timedelta(days=duration_value * 30)  # Приближенно 30 дней в месяце

        # Возвращаем cleaned_data, которое теперь включает поле duration
        return cleaned_data

class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ('name', 'duration', 'intensity', 'get_duration_in_days', 'get_duration_in_weeks', 'get_duration_in_months')
    list_filter = ('intensity',)  # Фильтр по интенсивности
    search_fields = ('name',)  # Поиск по названию курса

    # exclude = ('duration',)

admin.site.register(Course, CourseAdmin)