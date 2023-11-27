FROM php:8.1-apache
COPY src/ /var/www/html/
RUN echo "FLAG={NBCTF{pHP_p0p_Ch41N_F7W}}" > /flag.txt
RUN chown www-data:www-data /flag.txt
RUN chown -R www-data:www-data /var/www/html/
EXPOSE 80