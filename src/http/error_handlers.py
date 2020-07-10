from flask import jsonify

from src import logger


def err_404(error):
    return jsonify({'message': 'The requested URL was not found'}), 404


def err_405(error):
    return jsonify({'message': 'Method Not Allowed'}), 405


def err_500(error):
    logger.error('{0}'.format(error))
    return jsonify({'message': 'Server Error'}), 500


def err_validation(error):
    return jsonify({'message': error.messages}), 400