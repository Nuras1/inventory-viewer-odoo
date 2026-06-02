FROM odoo:18

RUN pip install requests

COPY ./addons /mnt/extra-addons
COPY ./odoo.conf /etc/odoo/odoo.conf

CMD ["odoo","-i","base","-c","/etc/odoo/odoo.conf"]