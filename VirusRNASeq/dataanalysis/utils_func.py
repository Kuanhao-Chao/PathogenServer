import os
import csv
import pandas
from django.conf import settings


def check_samples_txt_file(datadir):
    samples_txt_file_name = None
    samples_list_key = {}
    samples_txt_file = os.path.join(settings.MEDIA_ROOT, 'tmp', datadir, 'samples.csv')
    samples_txt_file_ans = os.path.exists(samples_txt_file)
    if samples_txt_file_ans:
        samples_txt_file_name = samples_txt_file
        read_ans = pandas.read_csv(samples_txt_file)
        samples_groups = read_ans['Groups'].unique()
        for i in samples_groups:
            group_samples = read_ans[read_ans['Groups'] == i]["ids"].tolist()
            samples_list_key[i] = group_samples
        print(samples_list_key)
        return (samples_txt_file_name, samples_list_key)

    else:
        return (samples_txt_file_name, samples_list_key)

def check_submission_time_file(datadir, sample_name, se_or_pe):
    submission_time_file = os.path.join(settings.MEDIA_ROOT, 'tmp', datadir, 'submision_time.txt')
    submission_time_file_ans = os.path.exists(submission_time_file)
    if submission_time_file_ans:
        return True
    else:
        return False


def check_first_qc(datadir, sample_name, se_or_pe):
    root_dir = os.path.join(settings.MEDIA_ROOT, 'tmp', datadir, 'QC', 'pre')
    if se_or_pe == 'pe':
        print("**** Inside check_first_qc function:")
        print("R1 html: ", os.path.join(root_dir, sample_name+".R1_fastqc.html"))
        print("R2 html: ", os.path.join(root_dir, sample_name+".R2_fastqc.html"))
        print("R1 zip: ", os.path.join(root_dir, sample_name+".R1_fastqc.zip"))
        print("R2 zip: ", os.path.join(root_dir, sample_name+".R2_fastqc.zip"))
        print("multiqc html: ", os.path.join(root_dir, sample_name+"_multiqc.html"))
        print("multiqc dir: ", os.path.join(
            root_dir, sample_name+"_multiqc_data"))
        r1_html = os.path.exists(os.path.join(root_dir, sample_name+".R1_fastqc.html"))
        r2_html = os.path.exists(os.path.join(root_dir, sample_name+".R2_fastqc.html"))
        r1_zip = os.path.exists(os.path.join(root_dir, sample_name+".R1_fastqc.zip"))
        r2_zip = os.path.exists(os.path.join(root_dir, sample_name+".R2_fastqc.zip"))
        multiqc_html = os.path.exists(os.path.join(root_dir, sample_name+"_multiqc.html"))
        multiqc_dir = os.path.exists(os.path.join(root_dir, sample_name+"_multiqc_data"))
        print("r1_html: ", r1_html)
        print("r2_html: ", r2_html)
        print("r1_zip: ", r1_zip)
        print("r2_zip: ", r2_zip)
        print("multiqc_html: ", multiqc_html)
        print("multiqc_dir: ", multiqc_dir)
        if r1_html and r2_html and r1_zip and r2_zip and multiqc_html and multiqc_dir:
            return True
        else:
            return False
    elif se_or_pe == 'se':
        # Will be added in the future
        return True


def check_trimming_qc(datadir, sample_name, se_or_pe):
    root_dir_trimmed_paired = os.path.join(settings.MEDIA_ROOT, 'tmp', datadir, "trimmed_paired")
    root_dir_trimmed_unpaired = os.path.join(
        settings.MEDIA_ROOT, 'tmp', datadir, "trimmed_unpaired")
    if se_or_pe == 'pe':
        print("**** Inside trimmomatic_pe_target function:")
        print("r1_paired: ", os.path.join(
            root_dir_trimmed_paired, sample_name+"_r1_paired.fastq.gz"))
        print("r2_paired: ", os.path.join(
            root_dir_trimmed_paired, sample_name+"_r2_paired.fastq.gz"))
        print("r1_unpaired: ", os.path.join(
            root_dir_trimmed_unpaired, sample_name+"_r1_unpaired.fastq.gz"))
        print("r2_unpaired: ", os.path.join(
            root_dir_trimmed_unpaired, sample_name+"_r2_unpaired.fastq.gz"))
        r1_paired = os.path.exists(os.path.join(
            root_dir_trimmed_paired, sample_name+"_r1_paired.fastq.gz"))
        r2_paired = os.path.exists(os.path.join(
            root_dir_trimmed_paired, sample_name+"_r2_paired.fastq.gz"))
        r1_unpaired = os.path.exists(os.path.join(
            root_dir_trimmed_unpaired, sample_name+"_r1_unpaired.fastq.gz"))
        r2_unpaired = os.path.exists(os.path.join(
            root_dir_trimmed_unpaired, sample_name+"_r2_unpaired.fastq.gz"))
        print("r1_paired: ", r1_paired)
        print("r2_paired: ", r2_paired)
        print("r1_unpaired: ", r1_unpaired)
        print("r2_unpaired: ", r2_unpaired)
        if r1_paired and r2_paired and r1_unpaired and r2_unpaired:
            return True
        else:
            return False
    elif se_or_pe == 'se':
        # Will be added in the future
        return True


def check_second_qc(datadir, sample_name, se_or_pe):
    root_dir = os.path.join(settings.MEDIA_ROOT, 'tmp', datadir, 'QC', 'post')
    if se_or_pe == 'pe':
        print("**** Inside check_first_qc function:")
        print("R1 paired html: ", os.path.join(
            root_dir, sample_name+"_r1_paired_fastqc.html"))
        print("R1 unpaired html: ", os.path.join(
            root_dir, sample_name+"_r1_unpaired_fastqc.html"))
        print("R2 paired html: ", os.path.join(
            root_dir, sample_name+"_r2_paired_fastqc.html"))
        print("R2 unpaired html: ", os.path.join(
            root_dir, sample_name+"_r2_unpaired_fastqc.html"))
        print("R1 paired zip: ", os.path.join(
            root_dir, sample_name+"_r1_paired_fastqc.zip"))
        print("R1 unpaired zip: ", os.path.join(
            root_dir, sample_name+"_r1_unpaired_fastqc.zip"))
        print("R2 paired zip: ", os.path.join(
            root_dir, sample_name+"_r2_paired_fastqc.zip"))
        print("R2 unpaired zip: ", os.path.join(
            root_dir, sample_name+"_r2_unpaired_fastqc.zip"))
        print("multiqc html: ", os.path.join(
            root_dir, sample_name+"_multiqc.html"))
        print("multiqc dir: ", os.path.join(
            root_dir, sample_name+"_multiqc_data"))
        r1_paired_html = os.path.exists(os.path.join(
            root_dir, sample_name+"_r1_paired_fastqc.html"))
        r1_unpaired_html = os.path.exists(os.path.join(
            root_dir, sample_name+"_r1_unpaired_fastqc.html"))
        r2_paired_html = os.path.exists(os.path.join(
            root_dir, sample_name+"_r2_paired_fastqc.html"))
        r2_unpaired_html = os.path.exists(os.path.join(
            root_dir, sample_name+"_r2_unpaired_fastqc.html"))
        r1_paired_zip = os.path.exists(os.path.join(
            root_dir, sample_name+"_r1_paired_fastqc.zip"))
        r1_unpaired_zip = os.path.exists(os.path.join(
            root_dir, sample_name+"_r1_unpaired_fastqc.zip"))
        r2_paired_zip = os.path.exists(os.path.join(
            root_dir, sample_name+"_r2_paired_fastqc.zip"))
        r2_unpaired_zip = os.path.exists(os.path.join(
            root_dir, sample_name+"_r2_unpaired_fastqc.zip"))
        multiqc_html = os.path.exists(os.path.join(
            root_dir, sample_name+"_multiqc.html"))
        multiqc_dir = os.path.exists(os.path.join(
            root_dir, sample_name+"_multiqc_data"))
        print("r1_paired_html: ", r1_paired_html)
        print("r1_unpaired_html: ", r1_unpaired_html)
        print("r2_paired_html: ", r2_paired_html)
        print("r2_unpaired_html: ", r2_unpaired_html)
        print("r1_paired_zip: ", r1_paired_zip)
        print("r1_unpaired_zip: ", r1_unpaired_zip)
        print("r2_paired_zip: ", r2_paired_zip)
        print("r2_unpaired_zip: ", r2_unpaired_zip)
        print("multiqc_html: ", multiqc_html)
        print("multiqc_dir: ", multiqc_dir)
        if r1_paired_html and r1_unpaired_html and r2_paired_html and r2_unpaired_html and r1_paired_zip and r1_unpaired_zip and r2_paired_zip and r2_unpaired_zip and multiqc_html and multiqc_dir:
            return True
        else:
            return False
    elif se_or_pe == 'se':
        # Will be added in the future
        return True


def check_read_subtraction_bwa_align(datadir, sample_name):
    root_dir = os.path.join(settings.MEDIA_ROOT, 'tmp', datadir, "Read_Subtraction", "bwa", "sam")
    print("bwa sam file: ", os.path.join(
        root_dir, sample_name+".sam"))
    bwa_read_subtraction_sam = os.path.exists(os.path.join(
        root_dir, sample_name+".sam"))
    print("bwa_read_subtraction_sam: ", bwa_read_subtraction_sam)
    if bwa_read_subtraction_sam:
        return True
    else:
        return False


def check_extract_non_host_reads_1(datadir, sample_name):
    root_dir = os.path.join(settings.MEDIA_ROOT, 'tmp', datadir, "Extract_non_host_reads", "bam")
    print("bwa bam file: ", os.path.join(
        root_dir, sample_name+".bam"))
    extract_non_host_reads_1_bam = os.path.exists(os.path.join(
        root_dir, sample_name+".bam"))
    print("extract_non_host_reads_1_bam: ", extract_non_host_reads_1_bam)
    if extract_non_host_reads_1_bam:
        return True
    else:
        return False

def check_extract_non_host_reads_2(datadir, sample_name):
    root_dir = os.path.join(settings.MEDIA_ROOT, 'tmp', datadir, "Extract_non_host_reads", "txt")
    print("bwa txt file: ", os.path.join(
        root_dir, sample_name+".txt"))
    extract_non_host_reads_2_txt = os.path.exists(os.path.join(
        root_dir, sample_name+".txt"))
    print("extract_non_host_reads_2_txt: ", extract_non_host_reads_2_txt)
    if extract_non_host_reads_2_txt:
        return True
    else:
        return False

def check_extract_non_host_reads_3(datadir, sample_name):
    root_dir = os.path.join(settings.MEDIA_ROOT, 'tmp', datadir, "Extract_non_host_reads", "unmapped_bam")
    print("bwa unmapped_bam file: ", os.path.join(
        root_dir, sample_name+".unmapped.bam"))
    extract_non_host_reads_3_unmapped_bam = os.path.exists(os.path.join(
        root_dir, sample_name+".unmapped.bam"))
    print("extract_non_host_reads_3_unmapped_bam: ", extract_non_host_reads_3_unmapped_bam)
    if extract_non_host_reads_3_unmapped_bam:
        return True
    else:
        return False

def check_extract_non_host_reads_4(datadir, sample_name):
    root_dir = os.path.join(settings.MEDIA_ROOT, 'tmp', datadir, "Extract_non_host_reads", "unmapped_fastq")
    extract_non_host_reads_4_unmapped_fastq_r1 = os.path.exists(os.path.join(root_dir, sample_name+".unmapped.R1.fastq"))
    extract_non_host_reads_4_unmapped_fastq_r2 = os.path.exists(os.path.join(root_dir, sample_name+".unmapped.R2.fastq"))
    print("extract_non_host_reads_4_unmapped_fastq_r1: ", extract_non_host_reads_4_unmapped_fastq_r1)
    print("extract_non_host_reads_4_unmapped_fastq_r2: ", extract_non_host_reads_4_unmapped_fastq_r2)
    if extract_non_host_reads_4_unmapped_fastq_r1 and extract_non_host_reads_4_unmapped_fastq_r2:
        return True
    else:
        return False

def get_pe_sample_name(se_or_pe, project_name, email, analysis_code):
    if se_or_pe == 'pe':
        datadir = os.path.join(settings.MEDIA_ROOT, 'tmp',
                            project_name + '_' + email + '_' + analysis_code)
        files = os.listdir(os.path.join(datadir, se_or_pe))
        sample_name = os.path.splitext(os.path.splitext(
            os.path.splitext(files[0])[0])[0])[0]
        return sample_name
    elif se_or_pe == 'se':
        pass

def check_end_time_file(datadir, sample_name, se_or_pe):
    end_time_file = os.path.join(settings.MEDIA_ROOT, 'tmp', datadir, 'end_time.txt')
    end_time_file_ans = os.path.exists(end_time_file)
    if end_time_file_ans:
        return True
    else:
        return False
