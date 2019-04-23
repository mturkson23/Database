from django.db import models

# https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models


class Project(models.Model):
    repository = models.CharField(max_length=200)
    study_title = models.CharField(max_length=200)
    pmid = models.CharField(max_length=200)
    assay_type = models.CharField(max_length=200)
    avg_spotlen = models.CharField(max_length=200)
    bioproject_name = models.CharField(max_length=200)
    bioproject = models.CharField(max_length=200)
    bioproject_links = models.CharField(max_length=200)
    mg_id = models.CharField(max_length=200)
    biosample = models.CharField(max_length=200)
    mg_rast_id = models.CharField(max_length=200)
    biosample_model = models.CharField(max_length=200)
    run = models.CharField(max_length=200)
    sra_sample = models.CharField(max_length=200)
    sra_study = models.CharField(max_length=200)
    sample_name = models.CharField(max_length=200)
    collection_date = models.CharField(max_length=200)
    experiment = models.CharField(max_length=200)
    library_source = models.CharField(max_length=200)
    library_layout = models.CharField(max_length=200)
    libraryselection = models.CharField(max_length=200)
    insert_size = models.CharField(max_length=200)
    library_name = models.CharField(max_length=200)
    centre_name = models.CharField(max_length=200)
    instrument = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    amplicon_target = models.CharField(max_length=200)
    load_date = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    ena_last_update = models.CharField(max_length=200)
    mbases = models.CharField(max_length=200)
    mbytes = models.CharField(max_length=200)
    organism = models.CharField(max_length=200)
    env_biome = models.CharField(max_length=200)
    env_feature = models.CharField(max_length=200)
    env_material = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    case_control = models.CharField(max_length=200)
    host_taxa_id = models.CharField(max_length=200)
    lat_ion = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    coordinate = models.CharField(max_length=200)
    physical_specimen_remaining = models.CharField(max_length=200)
    pregnant = models.CharField(max_length=200)
    consent = models.CharField(max_length=200)
    datastore_provider = models.CharField(max_length=200)
    isolation_source = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    antibiotic_regimen = models.CharField(max_length=200)
    birth_delivery = models.CharField(max_length=200)
    special_diet = models.CharField(max_length=200)
    disease_stage = models.CharField(max_length=200)
    host_body_mass_index = models.CharField(max_length=200)
    fastq_ftp = models.CharField(max_length=200)
    bp_count = models.CharField(max_length=200)
    seq_count = models.CharField(max_length=200)
