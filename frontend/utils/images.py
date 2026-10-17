
import base64
import urllib.parse


def encode_text_for_overlay(text):
    if not text:
        return ""

    encoded = base64.b64encode(
        text.encode("utf-8")
    ).decode("utf-8")

    return urllib.parse.quote(encoded)


def create_transformed_url(
    original_url,
    transformation_params,
    caption=None,
):
    if not original_url:
        return original_url

    if caption:
        encoded_caption = encode_text_for_overlay(caption)

        transformation_params = (
            f"l-text,ie-{encoded_caption},ly-N20,lx-20,"
            "fs-100,co-white,bg-000000A0,l-end"
        )

    if not transformation_params:
        return original_url

    parts = original_url.split("/")

    if len(parts) < 5 or "imagekit.io" not in parts[2]:
        return original_url

    base_url = "/".join(parts[:4])
    file_path = "/".join(parts[4:])

    return (
        f"{base_url}/tr:{transformation_params}/{file_path}"
    )