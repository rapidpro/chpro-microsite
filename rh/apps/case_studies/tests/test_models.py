from django.test import TestCase
from model_mommy import mommy


class CaseStudySimilarTests(TestCase):

    def test_not_self(self):
        one = mommy.make('case_studies.CaseStudy', published=True)
        assert one.similar() == []

    def test_only_published(self):
        one = mommy.make('case_studies.CaseStudy', published=True)
        two = mommy.make('case_studies.CaseStudy', published=True)
        three = mommy.make('case_studies.CaseStudy')
        assert one.similar() == [two]
        assert set(one.similar(only_published=False)) == set([two, three])
        assert set(three.similar()) == set([one, two])

    def test_count(self):
        one = mommy.make('case_studies.CaseStudy')
        mommy.make('case_studies.CaseStudy', published=True, _quantity=5)
        assert len(one.similar()) == 4
        assert len(one.similar(count=3)) == 3

    def test_use_case(self):
        one = mommy.make('case_studies.CaseStudy', make_m2m=True)
        use_cases = list(one.use_cases.all())
        mommy.make('case_studies.CaseStudy', published=True, _quantity=100)
        expected = mommy.make(
            'case_studies.CaseStudy', published=True, use_cases=use_cases[:1],
            _quantity=4)
        assert set(one.similar()) == set(expected)

    def test_use_case_partial(self):
        one = mommy.make('case_studies.CaseStudy', make_m2m=True)
        use_cases = list(one.use_cases.all())
        generic = mommy.make(
            'case_studies.CaseStudy', published=True, _quantity=50)
        expected = set(mommy.make(
            'case_studies.CaseStudy', published=True, use_cases=use_cases[:1],
            _quantity=3))
        similar = set(one.similar())
        assert similar >= expected
        extra = similar - expected
        assert len(extra) == 1
        assert extra.pop() in generic

    def test_use_case_no_duplicates(self):
        one = mommy.make(
            'case_studies.CaseStudy', published=True, make_m2m=True)
        use_cases = list(one.use_cases.all())
        two = mommy.make(
            'case_studies.CaseStudy', published=True, use_cases=use_cases)
        three = mommy.make(
            'case_studies.CaseStudy', published=True, use_cases=use_cases[:1])
        similar = one.similar()
        assert len(similar) == 2
        assert set(similar) == set([two, three])
