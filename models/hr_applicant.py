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
    interviewer_ids = fields.Many2many('res.users', string="Интервьюеры")

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

    registration_address_pdf = fields.Binary(string="Адрес прописки")
    registration_address_filename = fields.Char()

    residence_address_pdf = fields.Binary(string="Адрес проживания")
    residence_address_filename = fields.Char()

    email = fields.Char(string="Почта")
    
    bank_details_pdf = fields.Binary(string="Банковские реквизиты")
    bank_details_filename = fields.Char()

    # Авто-действие: при переходе на 2 стадию
    @api.onchange('stage_id')
    def _onchange_stage_notify_assistant(self):
        if self.stage_id.name == "Получение документов от кандидата":
            self._create_assistant_task()

    def _create_assistant_task(self):
        """Создать активность бизнес-ассистенту"""
        assistant = self.env.ref('hr_custom.business_assistant_user', raise_if_not_found=False)
        if not assistant:
            return

        self.activity_schedule(
            'mail.mail_activity_data_todo',
            user_id=assistant.id,
            summary="Собрать документы с кандидата",
            note="Пожалуйста, соберите все документы: диплом, резюме, УДО и др.",
            deadline=fields.Date.today() + fields.Date.to_date("3 days")
        )


    # PDF-файлы
    employment_contract_pdf = fields.Binary(string="Трудовой договор")
    employment_contract_filename = fields.Char()

    nda_pdf = fields.Binary(string="НДА")
    nda_filename = fields.Char()

    salary_agreement_pdf = fields.Binary(string="Соглашение о зарплате")
    salary_agreement_filename = fields.Char()

    # Шаблон приказа
    order_template = fields.Many2one('sign.template', string="Шаблон приказа")

    def action_sign_order(self):
        """Открытие документа для подписания"""
        self.ensure_one()
        template = self.order_template
        if not template:
            return
        return {
            'type': 'ir.actions.client',
            'tag': 'sign.Document',
            'params': {
                'template_id': template.id,
                'signers': [{'role': r.role_id.id, 'partner_id': self.partner_id.id}]
                if self.partner_id else [],
            }
        }
    

    # Stage 4
    contract_signed = fields.Boolean(string="ТД подписан")
    order_signed = fields.Boolean(string="Приказ подписан")
    nda_signed = fields.Boolean(string="НДА подписан")

    # Stage 5
    documents_transferred = fields.Boolean(string="Документы переданы сотруднику")
    document_transfer_date = fields.Date(string="Дата передачи документов")