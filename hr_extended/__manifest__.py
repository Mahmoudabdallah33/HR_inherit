
{
    'name' : 'hr_extended',
    'version' : '1.2',
    'summary': ' ',
    'sequence': 0,
    'description': """ HR Task From UD  """,
    'category': '',
    'website': ' ',
    'depends' : ['hr_contract','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_contract_form_view_inherit.xml',
    ],
    'demo': [     ],
    'installable': True,
    'application': True,

    'license': 'LGPL-3',
}
