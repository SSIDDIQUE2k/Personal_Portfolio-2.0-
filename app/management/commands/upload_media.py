from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
import os
from pathlib import Path


class Command(BaseCommand):
    help = 'Upload local media files to Railway storage'

    def add_arguments(self, parser):
        parser.add_argument(
            '--source',
            type=str,
            default='media',
            help='Source directory to upload from (default: media)'
        )

    def handle(self, *args, **options):
        source_dir = Path(options['source'])
        
        if not source_dir.exists():
            self.stdout.write(
                self.style.ERROR(f'Source directory {source_dir} does not exist')
            )
            return

        # Ensure storage directory exists
        storage_dir = Path(settings.MEDIA_ROOT)
        storage_dir.mkdir(parents=True, exist_ok=True)
        
        uploaded_count = 0
        
        # Walk through all files in source directory
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                source_file = Path(root) / file
                
                # Calculate relative path
                rel_path = source_file.relative_to(source_dir)
                dest_file = storage_dir / rel_path
                
                # Create destination directory if needed
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                
                # Copy file
                with open(source_file, 'rb') as f:
                    with open(dest_file, 'wb') as dest_f:
                        dest_f.write(f.read())
                
                uploaded_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Uploaded: {rel_path}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully uploaded {uploaded_count} files to {storage_dir}')
        )
