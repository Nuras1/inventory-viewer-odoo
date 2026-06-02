FROM odoo:18

USER root

RUN pip3 install --break-system-packages requests

COPY ./addons /mnt/extra-addons
COPY ./odoo.conf /etc/odoo/odoo.conf

CMD ["odoo","-c","/etc/odoo/odoo.conf"]