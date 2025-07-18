{
    'name': 'HR Customizations',
    'version': '1.0',
    'depends': ['hr', 'hr_recruitment'],
    'data': [
        'views/hr_employee_views.xml',
        'data/delete_default_stages.xml',  
        'data/stage_data.xml',
        'data/hr_job_data.xml',
        'data/hr_company_menu.xml',
        'data/hr_departments.xml',
        'views/hr_employee_documents_tab.xml',  
        'views/hr_applicant_form.xml',   
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
