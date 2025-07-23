# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    # 📌 Стадия 1: Получение решения о принятии в штат
    expected_salary = fields.Float(string="Ожидаемая зарплата")
    employment_date = fields.Date(string="Дата устройства")
    trial_start = fields.Date(string="Начало испытательного срока")
    trial_end = fields.Date(string="Окончание испытательного срока")
    phone = fields.Char(string="Телефон")
    recruiter_id = fields.Many2one('res.users', string="Специалист по подбору кадров")
    birth_date = fields.Date(string="Дата рождения")
    company_id = fields.Many2one('res.company', string="Компания")


    # 📌 Стадия 2: Получение документов от кандидата
    diploma_pdf = fields.Binary(string="Диплом")
    diploma_filename = fields.Char()
    
    attachment_pdf = fields.Binary(string="Приложение")
    attachment_filename = fields.Char()

    identity_pdf = fields.Binary(string="УДО")
    identity_filename = fields.Char()

    resume_pdf = fields.Binary(string="Резюме")
    resume_filename = fields.Char()

    certificate_pdf = fields.Binary(string="Сертификат")
    certificate_filename = fields.Char()

    registration_address = fields.Char(string="Адрес регистрации")

    residence_address = fields.Char(string="Адрес проживания")

    email = fields.Char(string="Почта")

    phone = fields.Char(string="Телефон")
    
    bank_details_pdf = fields.Char(string="Банковские реквизиты")

    