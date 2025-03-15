# Arquitectura

Kata Backend sigue una arquitectura **Hexagonal (Ports & Adapters)**, lo que permite una separación clara entre la lógica de negocio y las interfaces externas.

## Principios de la Arquitectura

La arquitectura Hexagonal se basa en los siguientes conceptos clave:

- **Dominios independientes**: La lógica de negocio está desacoplada de la infraestructura.
- **Puertos y Adaptadores**: Las interfaces externas interactúan con el core mediante puertos, evitando dependencias directas.
- **Facilidad de pruebas**: Separación clara entre capas facilita pruebas unitarias y de integración.

## Stack Tecnológico

El backend está construido utilizando las siguientes tecnologías:

- **Golang (Fiber)**: Framework web minimalista y eficiente para manejar peticiones HTTP.
- **PostgreSQL**: Base de datos relacional para almacenamiento persistente.
- **GORM**: ORM para interactuar con la base de datos de forma más sencilla.
- **GraphQL con gqlgen**: API basada en GraphQL para una comunicación eficiente.
- **Docker**: Contenedores para garantizar despliegues consistentes.
- **Terraform**: Infraestructura como código (IaC) para la gestión del entorno en la nube.