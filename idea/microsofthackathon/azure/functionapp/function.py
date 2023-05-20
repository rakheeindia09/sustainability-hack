import logging
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        prediction = req_body.get('prediction')
        current_temperature = req_body.get('temperature')
        current_lighting_level = req_body.get('lighting_level')

        if prediction is not None and current_temperature is not None and current_lighting_level is not None:
            temperature_adjustment, lighting_adjustment = adjust_energy_consumption_prediction(prediction)

            # Apply the adjustments to temperature and lighting levels
            adjusted_temperature = current_temperature + temperature_adjustment
            adjusted_lighting_level = current_lighting_level + lighting_adjustment

            set_temperature(adjusted_temperature)
            set_lighting_level(adjusted_lighting_level)

            response_payload = {
                'adjusted_temperature': adjusted_temperature,
                'adjusted_lighting_level': adjusted_lighting_level
            }

            return func.HttpResponse(
                json.dumps(response_payload),
                mimetype='application/json',
                status_code=200
            )
        else:
            return func.HttpResponse(
                'Prediction value, current temperature, or current lighting level not provided.',
                status_code=400
            )

    except Exception as e:
        logging.error(f'Error: {str(e)}')
        return func.HttpResponse(
            'An error occurred while processing the request.',
            status_code=500
        )

def adjust_energy_consumption_prediction(prediction):
    temperature_adjustment = 0
    lighting_adjustment = 0

    if prediction > 1000:
        temperature_adjustment = -5
        lighting_adjustment = -1
    else:
        temperature_adjustment = 5
        lighting_adjustment = 1

    return temperature_adjustment, lighting_adjustment

