# to log in to database
# ***********************************
import xmlrpc.client

url = 'http://localhost:8069/'
db = 'odoo16'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})
# ************************************

if uid:
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    records = [
        'اصل شهادة الميلاد',
        'اصل شهادة الجيش',
        'اصل المؤهل الدراسى',
        '6 صور شخصية',
        'صحيفة الحالة الجنائية',
        'كعب العمل',
        'طلب التعين',
        'نموذج 111 كشف طبى',
        'صورة رقم قومى سارى',
        'طبعة تامينية او استمارة 6',
        'صورة رخصة سارية'
    ]

    # Insert records using Odoo ORM
    for record in records:
        id = models.execute_kw(db, uid, password, 'hr.hiring.document', 'create', [{'name':record}])

