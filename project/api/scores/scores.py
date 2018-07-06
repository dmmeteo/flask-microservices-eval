from sqlalchemy import exc
from flask import Blueprint, jsonify, request

from project import db
from project.api.utils import authenticate
from project.api.scores.models import Score


scores_blueprint = Blueprint("scores", __name__)


@scores_blueprint.route('/scores', method=['GET'])
def get_all_scores():
    """Get all scores"""
    scores = Score.query.all()
    scores_list = []
    for score in scores:
        score_object = {
            'id': score.id,
            'user_id': score.user_id,
            'exercise_id': score.exercise_id,
            'created_at': score.created_at,
            'updated_at': score.updated_at
        }
        scores_list.append(score_object)
    response_object = {
        'status': 'success',
        'data': {
            'scores': scores_list
        }
    }
    return jsonify(response_object), 200
