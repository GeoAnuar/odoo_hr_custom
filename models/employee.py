from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'  # Наследуем от модели сотрудников
     
    iin = fields.Char(string='ИИН')
    contract_number = fields.Char(string='№ Трудового договора')
    hiring_date = fields.Date(string='Дата устройства')
    internal_department = fields.Many2one('hr.department', string='Отдел')
    internal_job_title = fields.Many2one('hr.job', string='Должность по внутренней структуре')
    time_of_job = fields.Char(string='Стаж')

   