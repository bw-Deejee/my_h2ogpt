from __future__ import annotations

from typing import Iterable

from gradio.themes.soft import Soft
from gradio.themes import Color, Size
from gradio.themes.utils import colors, sizes, fonts

h2o_yellow = Color(
    name="berry",
    c50="#ffeaf5",
    c100="#ffbfe2",
    c200="#ff95ce",
    c300="#ff6abb",
    c400="#ff40a7",
    c500="#ff1593",
    c600="#ea007e",
    c700="#bf0067",
    c800="#950050",
    c900="#6a0039",
    c950="#400022",
)
h2o_gray = Color(
    name="gray",
    c50="#f8f8f8",
    c100="#e5e5e5",
    c200="#cccccc",
    c300="#b2b2b2",
    c400="#999999",
    c500="#7f7f7f",
    c600="#666666",
    c700="#4c4c4c",
    c800="#333333",
    c900="#191919",
    c950="#0d0d0d",
)

text_xsm = Size(
    name="text_xsm",
    xxs="4px",
    xs="5px",
    sm="6px",
    md="7px",
    lg="8px",
    xl="10px",
    xxl="12px",
)

spacing_xsm = Size(
    name="spacing_xsm",
    xxs="1px",
    xs="1px",
    sm="1px",
    md="2px",
    lg="3px",
    xl="5px",
    xxl="7px",
)

radius_xsm = Size(
    name="radius_xsm",
    xxs="1px",
    xs="1px",
    sm="1px",
    md="2px",
    lg="3px",
    xl="5px",
    xxl="7px",
)


class H2oTheme(Soft):
    def __init__(
            self,
            *,
            primary_hue: colors.Color | str = h2o_yellow,
            secondary_hue: colors.Color | str = h2o_yellow,
            neutral_hue: colors.Color | str = h2o_gray,
            spacing_size: sizes.Size | str = sizes.spacing_md,
            radius_size: sizes.Size | str = sizes.radius_md,
            text_size: sizes.Size | str = sizes.text_lg,
            font: fonts.Font
                  | str
                  | Iterable[fonts.Font | str] = (
                    fonts.GoogleFont("Montserrat"),
                    "ui-sans-serif",
                    "system-ui",
                    "sans-serif",
            ),
            font_mono: fonts.Font
                       | str
                       | Iterable[fonts.Font | str] = (
                    fonts.GoogleFont("IBM Plex Mono"),
                    "ui-monospace",
                    "Consolas",
                    "monospace",
            ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        super().set(
            background_fill_primary_dark="*block_background_fill",
            block_background_fill_dark="*neutral_950",
            block_border_width='1px',
            block_border_width_dark='1px',
            block_label_background_fill="*primary_300",
            block_label_background_fill_dark="*primary_600",
            block_label_text_color="*neutral_950",
            block_label_text_color_dark="*neutral_950",
            block_radius="0 0 8px 8px",
            block_title_text_color="*neutral_950",
            block_title_text_color_dark="*neutral_950",
            body_background_fill="*neutral_50",
            body_background_fill_dark="*neutral_900",
            border_color_primary="*neutral_100",
            border_color_primary_dark="*neutral_700",
            button_border_width="1px",
            button_border_width_dark="1px",
            button_primary_text_color="*neutral_950",
            button_primary_text_color_dark="*neutral_950",
            button_primary_background_fill="*primary_500",
            button_primary_background_fill_dark="*primary_500",
            button_secondary_background_fill_hover_dark="*primary_700",
            button_secondary_border_color="*primary_500",
            button_secondary_border_color_dark="*primary_500",
            button_secondary_border_color_hover_dark="*primary_700",
            checkbox_label_text_color_selected_dark='#000000',
            # checkbox_label_text_size="*text_xs",  # too small for iPhone etc. but good if full large screen zoomed to fit
            checkbox_label_text_size="*text_sm",
            # radio_circle="""url("data:image/svg+xml,%3csvg viewBox='0 0 32 32' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3ccircle cx='32' cy='32' r='1'/%3e%3c/svg%3e")""",
            # checkbox_border_width=1,
            # heckbox_border_width_dark=1,
            link_text_color="#3344DD",
            link_text_color_hover="#3344DD",
            link_text_color_visited="#3344DD",
            link_text_color_dark="#74abff",
            link_text_color_hover_dark="#a3c8ff",
            link_text_color_active_dark="#a3c8ff",
            link_text_color_visited_dark="#74abff",
        )


class SoftTheme(Soft):
    def __init__(
            self,
            *,
            primary_hue: colors.Color | str = colors.indigo,
            secondary_hue: colors.Color | str = colors.indigo,
            neutral_hue: colors.Color | str = colors.gray,
            spacing_size: sizes.Size | str = sizes.spacing_md,
            radius_size: sizes.Size | str = sizes.radius_md,
            text_size: sizes.Size | str = sizes.text_md,
            font: fonts.Font
                  | str
                  | Iterable[fonts.Font | str] = (
                    fonts.GoogleFont("Montserrat"),
                    "ui-sans-serif",
                    "system-ui",
                    "sans-serif",
            ),
            font_mono: fonts.Font
                       | str
                       | Iterable[fonts.Font | str] = (
                    fonts.GoogleFont("IBM Plex Mono"),
                    "ui-monospace",
                    "Consolas",
                    "monospace",
            ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        super().set(
            checkbox_label_text_size="*text_sm",
        )


h2o_logo = '<?xml version="1.0" encoding="UTF-8"?>' \
	   '<svg enable-background="new 0 0 800 800" version="1.1" viewBox="0 0 800 800" xml:space="preserve" xmlns="http://www.w3.org/2000/svg">' \
	   '<path d="m526 418h-525v-417h792v417h-267m-273.6-317.05c-4.2748 1.3589-8.4906 2.9659-12.842 4.0011-3.7335 0.88809-4.8853 2.7074-4.7373 6.547 0.33008 8.5672 0.10315 17.156 0.10315 26.294h-15.039v32.501h15.039c0 2.5009-0.001343 4.327 1.99e-4 6.1531 0.022934 27.15-0.2681 54.305 0.16287 81.449 0.38734 24.398 14.463 42.054 37.34 46.471 8.5262 1.6463 17.546 1.261 26.312 0.96518 6.3715-0.21503 12.697-1.8053 18.281-2.6651v-32.693c-7.2202 1.0729-13.688 2.6248-20.204 2.8615-9.389 0.341-15.423-4.4808-17.77-13.615-1.1067-4.3074-1.7117-8.8605-1.7429-13.308-0.16724-23.818-0.087128-47.637-0.069214-71.456 9.46e-4 -1.2803 0.21283-2.5604 0.36792-4.307h37.099v-32.699h-37.64v-44.437c-8.4152 2.7224-16.151 5.2249-24.66 7.9389m-72.902 172.55c-23.971-1.0664-38.378-13.242-42.472-36.925-1.3441-7.7753-1.573-15.933-0.98335-23.816 1.52-20.322 14.02-43.727 46.256-42.648 8.764 0.29358 17.546 0.044555 26.444 0.044555v-32.243c-15.758 0-31.276-0.80899-46.68 0.17566-28.308 1.8094-49.708 15.346-62.008 41.237-11.935 25.122-12.064 51.29-3.3683 77.352 8.41 25.206 26.159 40.765 51.998 46.909 12.943 3.0775 26.127 3.1052 39.261 1.7567 8.6669-0.88992 17.249-2.6035 25.992-3.9674-0.72288-12.392-1.3773-23.611-1.975-33.857-10.698 2.0128-21.094 3.9689-32.463 5.982m356.68-94.239c-13.629-7.4287-28.328-9.5968-43.526-8.0745-16.253 1.628-30.604 7.8157-41.767 20.118-15.354 16.921-19.017 37.285-16.319 59.138 1.6705 13.528 7.1363 25.54 16.659 35.555 12.968 13.639 29.382 19.149 47.619 19.659 16.528 0.46307 32.108-3.1823 45.49-13.557 15.801-12.251 23.281-28.995 24.147-48.461 1.1974-26.914-7.39-49.458-32.303-64.377m81.036 82.232c0.25354-10.321 0.022583-20.683 0.89069-30.953 0.95557-11.305 4.0734-22.071 13.963-29.172 13.731-9.8594 31.284-3.4518 34.714 12.603 0.79334 3.7125 1.1872 7.5787 1.2068 11.377 0.12408 23.996 0.086121 47.992 0.12024 71.989 0.002503 1.7586 0.15173 3.5171 0.23157 5.2503h33.21c0.20081-0.64832 0.38031-0.9574 0.38037-1.2665 0.009582-29.327 0.45306-58.665-0.20428-87.978-0.28864-12.869-4.7301-24.88-15.186-33.544-15.413-12.771-43.875-12.437-60.543 0.69371-3.4398 2.7099-6.4309 5.9893-10.226 9.5698v-16.652c-9.2341 0-18.021 0.24631-26.784-0.10054-4.6028-0.18219-5.8714 1.212-5.8496 5.8435 0.18536 39.326 0.1059 78.654 0.10584 117.98v5.5009h33.972c0-13.572 0-26.857-3.05e-4 -41.143m-273.28 24.051c9.9832 11.76 22.894 17.673 38.033 19.557 14.882 1.8528 29.388 0.40607 44.241-3.5168-0.52124-9.3813-1.0224-18.402-1.537-27.664-6.2784 1.6731-11.928 3.7272-17.755 4.6307-19.011 2.9476-33.998-3.1873-40.324-23.57-3.1602-10.181-3.4713-20.56-0.80508-30.978 4.7677-18.63 17.493-28.309 36.381-26.871 6.1819 0.47072 12.253 2.397 18.698 3.7242 0.97064-7.6383 2.1074-15.35 2.7669-23.103 0.098938-1.1635-1.8144-3.2598-3.1729-3.6657-11.294-3.374-22.931-3.7845-34.594-3.1037-24.618 1.4369-41.811 13.643-51.578 36.243-5.2081 12.051-6.0067 24.789-5.2672 37.678 0.8476 14.772 5.0353 28.394 14.914 40.639z" fill="#fff"/>' \
	   '<path d="m252.79 100.85c8.1222-2.6082 15.858-5.1108 24.273-7.8332v44.437h37.64v32.699h-37.099c-0.15509 1.7466-0.36697 3.0267-0.36792 4.307-0.017914 23.819-0.098022 47.639 0.069214 71.456 0.03122 4.4474 0.63617 9.0005 1.7429 13.308 2.3471 9.1346 8.3811 13.956 17.77 13.615 6.5157-0.23669 12.984-1.7886 20.204-2.8615v32.693c-5.5845 0.85986-11.91 2.4501-18.281 2.6651-8.7664 0.29584-17.786 0.68115-26.312-0.96518-22.877-4.4173-36.953-22.073-37.34-46.471-0.43097-27.144-0.13994-54.299-0.16287-81.449-0.001542-1.8261-1.99e-4 -3.6522-1.99e-4 -6.1531h-15.039v-32.501h15.039c0-9.1376 0.22693-17.726-0.10315-26.294-0.14793-3.8396 1.0039-5.6589 4.7373-6.547 4.3518-1.0352 8.5676-2.6422 13.229-4.1068z" fill="#E2027B"/>' \
	   '<path d="m179.99 273.48c10.883-1.9846 21.279-3.9406 31.977-5.9535 0.59769 10.246 1.2521 21.464 1.975 33.857-8.7426 1.3639-17.325 3.0775-25.992 3.9674-13.133 1.3485-26.318 1.3208-39.261-1.7567-25.838-6.1439-43.588-21.703-51.998-46.909-8.6956-26.062-8.5663-52.23 3.3683-77.352 12.299-25.89 33.7-39.427 62.008-41.237 15.404-0.98465 30.923-0.17566 46.68-0.17566v32.243c-8.8979 0-17.68 0.24902-26.444-0.044555-32.236-1.0798-44.736 22.326-46.256 42.648-0.58965 7.8834-0.36079 16.041 0.98335 23.816 4.0942 23.683 18.501 35.859 42.959 36.897z" fill="#E2027C"/>' \
	   '<path d="m536.48 179.47c24.607 14.717 33.195 37.26 31.997 64.175-0.86603 19.466-8.3459 36.21-24.147 48.461-13.381 10.375-28.962 14.02-45.49 13.557-18.237-0.51092-34.651-6.0202-47.619-19.659-9.5227-10.015-14.989-22.027-16.659-35.555-2.6985-21.853 0.9649-42.217 16.319-59.138 11.163-12.302 25.514-18.49 41.767-20.118 15.198-1.5223 29.897 0.64578 43.832 8.2771m-55.426 93.005c16.761 13.175 39.65 8.1946 47.644-10.86 5.9772-14.247 6.8365-29.138 1.7002-43.894-4.6191-13.271-15.255-20.675-28.712-20.78-13.888-0.10896-24.41 7.158-29.617 20.333-3.599 9.1061-3.7924 18.56-2.6755 28.048 1.1629 9.8792 3.7866 19.291 11.66 27.154z" fill="#828282"/>' \
	   '<path d="m617.21 262c1.22e-4 13.785 1.22e-4 27.071 1.22e-4 40.643h-33.972v-5.5009c6.1e-5 -39.327 0.079529-78.655-0.10584-117.98-0.021789-4.6316 1.2468-6.0257 5.8496-5.8435 8.7634 0.34685 17.55 0.10054 26.784 0.10054v16.652c3.7953-3.5805 6.7864-6.86 10.226-9.5698 16.668-13.131 45.13-13.465 60.543-0.69371 10.456 8.664 14.898 20.676 15.186 33.544 0.65735 29.313 0.21387 58.65 0.20428 87.978-6.2e-5 0.30911-0.17957 0.6182-0.38037 1.2665h-33.21c-0.079834-1.7333-0.22906-3.4917-0.23157-5.2503-0.034118-23.996 0.003845-47.993-0.12024-71.989-0.019653-3.7983-0.41351-7.6645-1.2068-11.377-3.4305-16.054-20.983-22.462-34.714-12.603-9.8895 7.1011-13.007 17.867-13.963 29.172-0.8681 10.269-0.63715 20.631-0.8905 31.453z" fill="#828282"/>' \
	   '<path d="m343.7 285.29c-9.6425-11.981-13.83-25.603-14.678-40.375-0.73959-12.889 0.059021-25.628 5.2672-37.678 9.7672-22.6 26.96-34.806 51.578-36.243 11.664-0.68077 23.301-0.27029 34.594 3.1037 1.3586 0.40588 3.2719 2.5022 3.1729 3.6657-0.65945 7.7527-1.7962 15.465-2.7669 23.103-6.4453-1.3272-12.516-3.2535-18.698-3.7242-18.888-1.4383-31.613 8.2406-36.381 26.871-2.6662 10.418-2.3551 20.797 0.80508 30.978 6.3266 20.383 21.314 26.518 40.324 23.57 5.8275-0.90356 11.477-2.9576 17.755-4.6307 0.51459 9.2618 1.0158 18.283 1.537 27.664-14.853 3.9228-29.359 5.3695-44.241 3.5168-15.139-1.8847-28.05-7.7968-38.269-19.822z" fill="#828282"/>' \
	   '<path d="m480.8 272.22c-7.6153-7.6096-10.239-17.022-11.402-26.901-1.1169-9.4883-0.92346-18.942 2.6755-28.048 5.2071-13.175 15.729-20.442 29.617-20.333 13.457 0.10558 24.093 7.5098 28.712 20.78 5.1363 14.757 4.277 29.647-1.7002 43.894-7.994 19.054-30.883 24.034-47.902 10.607z" fill="#FEFEFE"/></svg>'


def get_h2o_title(title, description, visible_h2ogpt_qrcode):
    # NOTE: Check full width desktop, smallest width browser desktop, iPhone browsers to ensure no overlap etc.
    ret = f"""<div style="float:left; justify-content:left; height: 80px; width: 195px; margin-top:0px">
                    {description}
                </div>
                <div style="display:flex; justify-content:center; margin-bottom:30px; margin-right:330px;">
                    <div style="height: 30px; width: 100px; margin-right:20px;">{h2o_logo}</div>
                    <h1 style="line-height:60px">{title}</h1>
                </div>
                """
    if visible_h2ogpt_qrcode:
        ret += """
                <div style="float:right; height: 80px; width: 80px; margin-top:-100px">
                    <img src="https://raw.githubusercontent.com/h2oai/h2ogpt/main/docs/h2o-qr.png">
                </div>
                """
    return ret


def get_simple_title(title, description):
    return f"""{description}<h1 align="center"> {title}</h1>"""


def get_dark_js() -> str:
    return """
        if (document.querySelectorAll('.dark').length) {
            document.querySelectorAll('.dark').forEach(el => el.classList.remove('dark'));
        } else {
            document.querySelector('body').classList.add('dark');
        }
    """


def get_heap_js(heapAppId: str) -> str:
    return (
        """globalThis.window.heap=window.heap||[],heap.load=function(e,t){window.heap.appid=e,window.heap.config=t=t||{};var r=document.createElement("script");r.type="text/javascript",r.async=!0,r.src="https://cdn.heapanalytics.com/js/heap-"+e+".js";var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(r,a);for(var n=function(e){return function(){heap.push([e].concat(Array.prototype.slice.call(arguments,0)))}},p=["addEventProperties","addUserProperties","clearEventProperties","identify","resetIdentity","removeEventProperty","setEventProperties","track","unsetEventProperty"],o=0;o<p.length;o++)heap[p[o]]=n(p[o])};"""
        f"""heap.load("{heapAppId}");""")


def wrap_js_to_lambda(num_params: int, *args: str) -> str:
    """
    Generates a JS code representing JS lambda that wraps all given '*args' code strings.
    The lambda function has number of parameters based on 'num_params' and returns them
    without modification in an array. Lambda with zero parameters returns an empty array.
    """
    params = ", ".join([f"p{i}" for i in range(num_params)])
    newline = "\n"
    return f"""
        ({params}) => {{
            {newline.join([a for a in args if a is not None])}
            return [{params}];
        }}
    """
