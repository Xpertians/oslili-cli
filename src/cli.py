import argparse
from oslili import LicenseAndCopyrightIdentifier


def main():
    msg = 'Identify open source license and copyright statements'
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('file_path', help='Path to the file to analyze')
    args = parser.parse_args()

    with open(args.file_path, 'r') as f:
        text = f.read()

    identifier = LicenseAndCopyrightIdentifier()
    license_spdx_code, license_proba = identifier.identify_license(text)
    print(f'License: {license_spdx_code} ({license_proba:.2f} probability)')
    copyrights = identifier.copyright_extraction(text)
    print(f'Copyrights: {copyrights}')
    year_range, statement = identifier.identify_copyright(text)
    if year_range is None:
        print('year: None')
    if statement is None:
        print('statement: None')
    if statement:
        if None not in statement:
            print(f'Copyright: {statement}')


if __name__ == '__main__':
    main()