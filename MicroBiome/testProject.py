from django.test import TestCase
from MicroBiome.models import Project

class ProjectTestCase(TestCase):
    def testProject(self):
        project = Project(
            repository_id="REPO1", 
            study_title="TITLE",
            study_link="LINK",
            assay_type="ASSAY_TYPE",
            technology="TECH",
            country="GHANA",
            disease="DISEASE",
            study_design="DESIGN",
            body_site="SITE",
            platform="PLATFORM",
            participant_features="FEATURES",
            library_layout="LAYOUT",
            lon_lat="LON_LAT",
            sample_type="SAMPLE_TYPE",
            collection_date="COLLECTION_DATE",
            ethnicity="ETHNICITY",
            urbanzation="",
            region="",
            city="ACCRA",
            target_amplicon="AMPLICON",
            diet="DIET",
            sample_number="01",
            tags="02")

        self.assertEqual(project.repository_id, "REPO1")
        self.assertEqual(project.study_title, "TITLE")
        self.assertEqual(project.study_link, "LINK")
        self.assertEqual(project.assay_type, "ASSAY_TYPE")
        self.assertEqual(project.technology, "TECH")
        self.assertEqual(project.country, "GHANA")
        self.assertEqual(project.disease, "DISEASE")
        self.assertEqual(project.study_design, "DESIGN")
        self.assertEqual(project.body_site, "SITE")
        self.assertEqual(project.platform, "PLATFORM")
        self.assertEqual(project.participant_features, "FEATURES")
        self.assertEqual(project.library_layout, "LAYOUT")
        self.assertEqual(project.lon_lat, "LON_LAT")
        self.assertEqual(project.sample_type, "SAMPLE_TYPE")
        self.assertEqual(project.collection_date, "COLLECTION_DATE")
        self.assertEqual(project.ethnicity, "ETHNICITY")
        self.assertEqual(project.urbanzation, "URBANIZATION")
        self.assertEqual(project.region, "REGION")
        self.assertEqual(project.city, "ACCRA")
        self.assertEqual(project.target_amplicon, "AMPLICON")
        self.assertEqual(project.diet, "DIET")
        self.assertEqual(project.sample_number, "01")
        self.assertEqual(project.tags, "02")

