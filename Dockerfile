FROM odoo:18

COPY ./addons /mnt/extra-addons
COPY ./odoo.conf /etc/odoo/odoo.conf

CMD ["odoo","-i","base","-c","/etc/odoo/odoo.conf"]