import logging
from mailersend import emails
from app.domain.models.reservation import Reservation
from app.domain.models.showtime import Showtime
from app.domain.models.movie import Movie
from datetime import datetime
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


api_key = os.getenv("MAILERSEND_API_KEY")
mail_from = {
    "name": "Cinema",
    "email": "test@trial-jy7zpl92qw545vx6.mlsender.net"
}


def format_showtime(showtime_str):
    showtime_dt = datetime.fromisoformat(showtime_str)
    return showtime_dt.strftime("%Y-%m-%d"), showtime_dt.strftime("%H:%M")


def generate_html_content(variables, is_confirmation=True):
    """Generar el HTML para confirmación o cancelación."""
    title = "Confirmación de Reserva - Cinema" if is_confirmation else "Cancelación de Reserva - Cinema"
    message = (
        "¡Su reserva ha sido confirmada exitosamente!"
        if is_confirmation
        else "Lamentamos informarle que su reserva ha sido cancelada."
    )
    seats_section = (
        f"""
        <p><strong>Asientos:</strong></p>
        <ul style="padding-left: 20px;">
            {variables.get('seats', '')}
        </ul>
        """ if is_confirmation else ""
    )

    info_section = (
        """
        <div style="background-color: #e8f4f8; padding: 15px; border-radius: 5px; margin: 20px 0;">
            <h4 style="color: #2c3e50; margin-top: 0;">Información Importante:</h4>
            <ul style="padding-left: 20px;">
                <li>Por favor llegue 15 minutos antes de la función</li>
                <li>Presente este correo en la taquilla para retirar sus entradas</li>
                <li>No se permiten cambios de horario una vez confirmada la reserva</li>
            </ul>
        </div>
        """ if is_confirmation else ""
    )

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
            <h2 style="color: #2c3e50;">{title}</h2>
            <p>Estimado/a {variables['user_name']},</p>
            
            <p>{message}</p>
            
            <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0;">
                <h3 style="color: #2c3e50; margin-top: 0;">Detalles de su Reserva:</h3>
                <p><strong>Número de Reserva:</strong> #{variables['reservation_id']}</p>
                <p><strong>Película:</strong> {variables['movie_title']}</p>
                <p><strong>Fecha:</strong> {variables['show_date']}</p>
                <p><strong>Hora:</strong> {variables['show_time']}</p>
                {seats_section}
            </div>
            
            {info_section}
            
            <p>¡Gracias por elegirnos!</p>
            
            <p style="color: #666;">Saludos cordiales,<br>El equipo de Cinema</p>
        </div>
    </body>
    </html>
    """


def send_email(recipient, subject, html_content):
    """Enviar email con HTML."""
    mailer = emails.NewEmail(api_key)

    mail_body = {
        "from": mail_from,
        "to": recipient,
        "subject": subject,
        "html": html_content,
    }

    logger.info(f"Enviando email a {recipient[0]['email']}")

    try:
        response = mailer.send(mail_body)
        logger.info(
            f"Email enviado con éxito. Código de respuesta: {response}")
    except Exception as e:
        logger.error(f"Ocurrió un error al enviar el email: {e}")


def send_confirmed_reservation_email(reservation: Reservation, showtime: Showtime, movie: Movie):
    """Enviar correo de confirmación de reserva."""
    logger.info(
        f"Enviando email de confirmación para la reserva {reservation.id}")

    recipient = [{
        "name": reservation.user_name,
        "email": reservation.user_email
    }]

    show_date, show_time = format_showtime(showtime.start_time)

    seats_html = "".join(
        [f"<li>Fila {seat['row']}, Asiento {seat['number']}</li>" for seat in reservation.seats]
    )

    variables = {
        "user_name": reservation.user_name,
        "reservation_id": reservation.id,
        "movie_title": movie.title,
        "show_date": show_date,
        "show_time": show_time,
        "seats": seats_html
    }

    html_content = generate_html_content(variables, is_confirmation=True)
    send_email(recipient, subject="Confirmación de Reserva - Cinema",
               html_content=html_content)

    logger.info(
        f"Email de confirmación enviado para la reserva {reservation.id}")


def send_cancelled_reservation_email(reservation: Reservation, showtime: Showtime, movie: Movie):
    """Enviar correo de cancelación de reserva."""
    logger.info(
        f"Enviando email de cancelación para la reserva {reservation.id}")

    recipient = [{
        "name": reservation.user_name,
        "email": reservation.user_email
    }]

    show_date, show_time = format_showtime(showtime.start_time)

    variables = {
        "user_name": reservation.user_name,
        "reservation_id": reservation.id,
        "movie_title": movie.title,
        "show_date": show_date,
        "show_time": show_time
    }

    html_content = generate_html_content(variables, is_confirmation=False)
    send_email(recipient, subject="Cancelación de Reserva - Cinema",
               html_content=html_content)

    logger.info(
        f"Email de cancelación enviado para la reserva {reservation.id}")
