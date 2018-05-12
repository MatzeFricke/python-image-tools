#!/usr/bin/python
import argparse
import piexif
import sys


def print_exif_tag(_exif_dict, _tag):
    if hasattr(piexif.ExifIFD,_tag):
        tmp_tag = getattr(piexif.ExifIFD, _tag)
        print("{}({})\t{}".format(_tag, tmp_tag, _exif_dict["Exif"][tmp_tag]))
        return
    else:
        print("File did not contain tag with name {}".format(_tag))


def get_name_for_tag(_tag):
    for idf in piexif.TAGS:
        idf_dict = piexif.TAGS[idf]
        if _tag in idf_dict:
            return idf_dict[_tag]["name"]
    return 0


def get_tag_for_name(_name):
    print("TODO: implement me")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prints one or multiple EXIF information tags.",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "input",
        default=sys.stdin,
        help="Input File Path"
    )
    parser.add_argument(
        "-a",
        "--all",
        help="Displays all EXIF tags",
        action='store_true',
        default=False
    )
    parser.add_argument(
        '-t',
        '--tags',
        nargs='+',
        help="Specifies the EXIF tags that should be displayed"
    )
    parser.add_argument(
        '-ti',
        '--tagsById',
        nargs='+',
        help="Specifies the EXIF tag IDs that should be displayed"
    )

    args = parser.parse_args()

    # Load exif from inputfile
    exif_dict = piexif.load(args.input)

    if args.tags:
        for tag in args.tags:
            print_exif_tag(exif_dict, tag)

    if args.all:
        for ifd_name in exif_dict:
            if ifd_name == "thumbnail":
                continue
            print("\n{0} IFD:".format(ifd_name))

            for key in exif_dict[ifd_name]:
                key_name = get_name_for_tag(key)
                try:
                    print("{}({})\t{}".format(key_name,key, exif_dict[ifd_name][key][:10]))
                except:
                    print("{}({})\t{}".format(key_name, key, exif_dict[ifd_name][key]))
