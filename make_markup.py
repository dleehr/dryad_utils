__author__ = 'dan'
# coding=UTF-8


journal_name = ""
journal_url = ""
cover_image = ""

def render(journal_name, journal_url, cover_image):
    markup = "\
                    <xsl:when test='$journal-name = \"" + journal_name + "\"'>\n\
                        <a target=\"_blank\">\n\
                            <xsl:attribute name=\"href\">\n\
                                <xsl:choose>\n\
                                    <xsl:when test=\"contains($article-doi,'doi:')\">\n\
                                        <xsl:value-of\n\
                                                select=\"concat('http://dx.doi.org/', substring-after($article-doi, 'doi:'))\"/>\n\
                                    </xsl:when>\n\
                                    <xsl:otherwise>\n\
                                        <xsl:value-of\n\
                                                select=\"string('" + journal_url + "')\"/>\n\
                                    </xsl:otherwise>\n\
                                </xsl:choose>\n\
                            </xsl:attribute>\n\
                            <img class=\"pub-cover\" id=\"journal-logo\" src=\"/themes/Dryad/images/coverimages/" + cover_image + "\"\n\
                                 alt=\"" + journal_name +" cover\"/>\n\
                        </a>\n\
                    </xsl:when>"
    return markup


gms_journals = (
    ("GMS German Plastic, Reconstructive and Aesthetic Surgery", "http://www.egms.de/dynamic/de/journals/gpras/index.htm", "logo_gpras.png"),
    ("GMS Infectious Diseases", "http://www.egms.de/dynamic/en/journals/id/index.htm", "logo_id.png"),
    ("GMS Interdisciplinary Plastic and Reconstructive Surgery DGPW", "http://www.egms.de/dynamic/en/journals/iprs/", "logo_iprs_klein.png"),
    ("GMS Onkologische Rehabilitation und Sozialmedizin","http://www.egms.de/dynamic/en/journals/ors/index.htm", "logo_dgho.png"),
    ("GMS Zeitschrift für Medizinische Ausbildung","http://www.egms.de/dynamic/en/journals/zma/index.htm", "logo_gma_klein.png"),
    ("GMS Zeitschrift zur Förderung der Qualitätssicherung in medizinischen Laboratorien", "http://www.egms.de/dynamic/en/journals/lab/", "logo_lab.png")

)

for journal in gms_journals:
    print render(journal[0], journal[1], journal[2])