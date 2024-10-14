from nicegui import ui
from Units.Temperature import Temperature
from Units.Weight import Weight
from Units.Length import Length


def convert():
    global result_label, convert_result, reset_button

    # clear labels and inputs
    clear_inputs()

    if tabs.value == "Temperature":
        value = temperature_input.value
        from_unit = temperature_from_input.value
        to_unit = temperature_to_input.value

        temperature = Temperature(value, from_unit, to_unit)
        result = temperature.convert_temperature()

        result_label = ui.label("Result of your calculation").style(
            "font-family: 'Comic Sans MS'; font-weight: bold"
        )
        convert_result = ui.label(
            f"{value}{temperature.measure_units[from_unit]} = {int(result)}{temperature.measure_units[to_unit]}"
        ).style("font-family: 'Comic Sans MS'; font-size: 24px; font-weight: bold")

    if tabs.value == "Weight":
        value = weight_input.value
        from_unit = weight_from_input.value
        to_unit = weight_to_input.value

        weight = Weight(value, from_unit, to_unit)
        result = weight.convert_weight()

        result_label = ui.label("Result of your calculation").style(
            "font-family: 'Comic Sans MS'; font-weight: bold"
        )
        convert_result = ui.label(
            f"{value}{weight.measure_units[from_unit]} = {float(result)}{weight.measure_units[to_unit]}"
        ).style("font-family: 'Comic Sans MS'; font-size: 24px; font-weight: bold")

    reset_button = ui.button("Reset", on_click=reset_page).style(
        "font-family: 'Comic Sans MS'"
    )


def hide_elements(labels, inputs, button):
    # hide labels
    for label in labels:
        label.style("display: none")

    # hide inputs
    for input_field in inputs:
        input_field.style("display: none")

    # hide button
    button.style("display: none")


def clear_inputs():  # remove labels and input
    if tabs.value == "Length":
        hide_elements(
            [length_input_label, length_from_input_label, length_to_input_label],
            [length_input, length_to_input, length_from_input],
            length_convert_button,
        )

    if tabs.value == "Weight":
        hide_elements(
            [weight_input_label, weight_from_input_label, weight_to_input_label],
            [weight_input, weight_to_input, weight_from_input],
            weight_convert_button,
        )

    if tabs.value == "Temperature":
        hide_elements(
            [
                temperature_input_label,
                temperature_from_input_label,
                temperature_to_input_label,
            ],
            [temperature_input, temperature_to_input, temperature_from_input],
            temperature_convert_button,
        )


def reset_inputs(labels, inputs, button):
    # show hidden labels
    for label in labels:
        label.style("display: block")

    # show hidden inputs
    for input_field in inputs:
        input_field.style("display: block")

    # reset input values to empty
    for input_field in inputs:
        input_field.set_value("")

    # show hidden button
    button.style("display: block")


def reset_page():
    global result_label, convert_result, reset_button

    if tabs.value == "Length":
        reset_inputs(
            [length_input_label, length_from_input_label, length_to_input_label],
            [length_input, length_from_input, length_to_input],
            length_convert_button,
        )

    if tabs.value == "Weight":
        reset_inputs(
            [weight_input_label, weight_from_input_label, weight_to_input_label],
            [weight_input, weight_from_input, weight_to_input],
            weight_convert_button,
        )

    if tabs.value == "Temperature":
        reset_inputs(
            [
                temperature_input_label,
                temperature_from_input_label,
                temperature_to_input_label,
            ],
            [temperature_input, temperature_from_input, temperature_to_input],
            temperature_convert_button,
        )

    # To make sure that elements are not visibly AND invisibly created
    # hence increasing the card's height
    for element in [result_label, reset_button, convert_result]:
        if element:
            element.remove(element)

    ui.run()


with ui.card().classes("fixed-center").style("height: 560px"):
    ui.label("Unit Converter").style(
        "font-family: 'Comic Sans MS'; font-size: 24px; font-weight: bold"
    )
    with ui.tabs() as tabs:
        ui.tab("Length").style("font-family: 'Comic Sans MS'")
        ui.tab("Weight").style("font-family: 'Comic Sans MS'; font-weight: bold;")
        ui.tab("Temperature").style("font-family: 'Comic Sans MS'; font-weight: bold;")

    with ui.tab_panels(tabs, value="Length") as panels:
        with ui.tab_panel("Length"):
            # with ui.card().style("width: 260px"):
            length_input_label = ui.label("Enter the length to convert").style(
                "font-family: 'Comic Sans MS'; font-weight: bold; font-size: 15px"
            )
            length_input = ui.input(placeholder="Length value").style(
                "font-family: 'Comic Sans MS'"
            )

            length_from_input_label = ui.label("Unit to convert from").style(
                "font-family: 'Comic Sans MS'; font-weight: bold; font-size: 17px"
            )
            length_from_input = ui.input(placeholder="From unit (e.g., meter)").style(
                "font-family: 'Comic Sans MS'"
            )

            length_to_input_label = ui.label("Unit to convert to").style(
                "font-family: 'Comic Sans MS'; font-weight: bold; font-size: 15px"
            )
            length_to_input = ui.input(placeholder="To unit (e.g., centimeter)").style(
                "font-family: 'Comic Sans MS'"
            )

            length_convert_button = ui.button("Convert", on_click=convert).style(
                "font-family: 'Comic Sans MS'"
            )

        with ui.tab_panel("Weight"):
            # with ui.card():
            weight_input_label = ui.label("Enter the weight to convert").style(
                "font-family: 'Comic Sans MS'; font-weight: bold; font-size: 15px"
            )
            weight_input = ui.input(placeholder="Weight value").style(
                "font-family: 'Comic Sans MS'"
            )

            weight_from_input_label = ui.label("Unit to convert from").style(
                "font-family: 'Comic Sans MS'; font-weight: bold; font-size: 15px"
            )
            weight_from_input = ui.select(
                options=list(Weight.measure_units.keys()), with_input=True
            )

            weight_to_input_label = ui.label("Unit to convert to").style(
                "font-family: 'Comic Sans MS'; font-weight: bold; font-size: 15px"
            )
            weight_to_input = ui.select(
                options=list(Weight.measure_units.keys()), with_input=True
            )

            weight_convert_button = ui.button("Convert", on_click=convert).style(
                "font-family: 'Comic Sans MS'"
            )

        with ui.tab_panel("Temperature"):
            # with ui.card():
            temperature_input_label = ui.label(
                "Enter the temperature to convert"
            ).style("font-family: 'Comic Sans MS'; font-weight: bold; font-size: 15px")
            temperature_input = ui.input(placeholder="Temperature value").style(
                "font-weight: bold"
            )

            temperature_from_input_label = ui.label("Unit to convert from").style(
                "font-family: 'Comic Sans MS'; font-weight: bold; font-size: 15px"
            )
            temperature_from_input = ui.select(
                options=list(Temperature.measure_units.keys()), with_input=True
            )

            temperature_to_input_label = ui.label("Unit to convert to").style(
                "font-family: 'Comic Sans MS'; font-weight: bold; font-size: 15px"
            )
            temperature_to_input = ui.select(
                options=list(Temperature.measure_units.keys()), with_input=True
            )

            temperature_convert_button = ui.button("Convert", on_click=convert).style(
                "font-family: 'Comic Sans MS'"
            )

ui.run()