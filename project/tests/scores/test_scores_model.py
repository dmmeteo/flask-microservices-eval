from project import db
from project.api.scores.models import Score
from project.tests.base import BaseTestCase
from project.tests.utils import add_score


class TestScoreModel(BaseTestCase):

    def test_add_score(self):
        score = add_score(1, 1, True)
        self.assertTrue(score.id)
        self.assertEqual(score.user_id, 1)
        self.assertEqual(score.exercise_id, 1)
        self.assertTrue(score.created_at)
        self.assertTrue(score.updated_at)

    def test_all_scores(self):
        """Ensure get all scores behaves correctly"""
        add_score(1, 11, True)
        add_score(2, 22, False)
        with self.client:
            response = self.client.get('/scores')
            data = json.loads(response.data.decode())
            scores_data = data['data']['scores']
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(scores_data), 2)
            self.assertEqual(1, scores_data[0]['user_id'])
            self.assertEqual(2, scores_data[1]['user_id'])
            self.assertEqual(11, scores_data[0]['exercise_id'])
            self.assertEqual(22, scores_data[1]['exercise_id'])
            self.assertTrue(scores_data[0]['correct'])
            self.assertFalse(scores_data[1]['correct'])
            self.assertTrue('created_at' in scores_data[0])
            self.assertTrue('created_at' in scores_data[1])
            self.assertTrue('updated_at' in scores_data[0])
            self.assertTrue('updated_at' in scores_data[1])
            self.assertIn('success', data['status'])
