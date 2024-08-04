Feature: Agregar vehículo

  Scenario: Agregar un vehiculo
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Aplasta el botón agregar
    And Rellenar el campo Marca Chevrolet
    And Rellenar el campo Modelo Camioneta
    And Rellenar el campo Placa ASD-1457
    And Rellenar el campo Año 2010
    And Rellenar el campo Kilometraje 14000
    And Seleccionar el tipo de combustible Gasolina
    And Rellenar el campo Peso 15000
    And Seleccionar la foto del vehiculo C:\Users\cesar\OneDrive\Desktop\req\carro.jpg
    Then Aplastar el boton para guardar el vehiculo
    And Visualizar el auto guardado

  Scenario: Ingresar una placa incorrecta
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Aplasta el botón agregar
    And Rellenar el campo Marca Chevrolet
    And Rellenar el campo Modelo Camioneta
    And Rellenar el campo Placa AS1457
    And Rellenar el campo Año 2010
    And Rellenar el campo Kilometraje 14000
    And Seleccionar el tipo de combustible Gasolina
    And Rellenar el campo Peso 15000
    And Seleccionar la foto del vehiculo C:\Users\cesar\OneDrive\Desktop\req\carro.jpg
    Then Aplastar el boton para guardar el vehiculo
    And Visualizar el auto guardado

  Scenario: Ingresar un año incorrecto
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Aplasta el botón agregar
    And Rellenar el campo Marca Chevrolet
    And Rellenar el campo Modelo Camioneta
    And Rellenar el campo Placa ASD-1457
    And Rellenar el campo Año 20104
    And Rellenar el campo Kilometraje 14000
    And Seleccionar el tipo de combustible Gasolina
    And Rellenar el campo Peso 15000
    And Seleccionar la foto del vehiculo C:\Users\cesar\OneDrive\Desktop\req\carro.jpg
    Then Aplastar el boton para guardar el vehiculo
    And Visualizar el auto guardado

  Scenario: Ingresar un kilometraje incorrecto
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Aplasta el botón agregar
    And Rellenar el campo Marca Chevrolet
    And Rellenar el campo Modelo Camioneta
    And Rellenar el campo Placa ASD-1457
    And Rellenar el campo Año 2010
    And Rellenar el campo Kilometraje -14000
    And Seleccionar el tipo de combustible Gasolina
    And Rellenar el campo Peso 15000
    And Seleccionar la foto del vehiculo C:\Users\cesar\OneDrive\Desktop\req\carro.jpg
    Then Aplastar el boton para guardar el vehiculo
    And Visualizar el auto guardado

  Scenario: Ingresar un peso incorrecto
    Given Se inicia el navegador
    When Entra a la seccion vehiculo
    And Aplasta el botón agregar
    And Rellenar el campo Marca Chevrolet
    And Rellenar el campo Modelo Camioneta
    And Rellenar el campo Placa ASD-1457
    And Rellenar el campo Año 2010
    And Rellenar el campo Kilometraje 14000
    And Seleccionar el tipo de combustible Gasolina
    And Rellenar el campo Peso -15000
    And Seleccionar la foto del vehiculo C:\Users\cesar\OneDrive\Desktop\req\carro.jpg
    Then Aplastar el boton para guardar el vehiculo
    And Visualizar el auto guardado
