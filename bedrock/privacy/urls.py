# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from django.urls import path

from bedrock.mozorg.util import page
from bedrock.privacy import views

urlpatterns = (
    path("", views.privacy, name="privacy"),
    page("principles/", "privacy/principles.html", ftl_files=["privacy/principles", "privacy/index"]),
    path("faq/", views.FAQView.as_view(), name="privacy.faq"),
    page("email/", "privacy/email.html", active_locales=["en-US", "de", "fr"]),
    path("firefox/", views.firefox_notices, name="privacy.notices.firefox"),
    path("firefox-focus/", views.firefox_focus_notices, name="privacy.notices.firefox-focus"),
    # bug 1319207 - special URL for Firefox Focus in de locale
    path("firefox-klar/", views.firefox_focus_notices, name="privacy.notices.firefox-klar"),
    path("thunderbird/", views.thunderbird_notices, name="privacy.notices.thunderbird"),
    path("websites/", views.websites_notices, name="privacy.notices.websites"),
    page("websites/data-preferences/", "privacy/data-preferences.html", ftl_files=["privacy/data-preferences"]),
    page("websites/cookie-settings/", "privacy/cookie-settings.html", ftl_files=["privacy/cookie-settings"]),
    path("mdn-plus/", views.mdn_plus, name="privacy.notices.mdn-plus"),
    path("ad-targeting-guidelines/", views.ad_targeting_guidelines, name="privacy.notices.ad-targeting-guidelines"),
    path("subscription-services/", views.subscription_services, name="privacy.notices.subscription-services"),
    path("mozilla-accounts/", views.mozilla_accounts, name="privacy.notices.mozilla-accounts"),
    page("archive/", "privacy/archive/index.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox/2006-10/", "privacy/archive/firefox-2006-10.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox/2008-06/", "privacy/archive/firefox-2008-06.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox/2009-01/", "privacy/archive/firefox-2009-01.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox/2009-09/", "privacy/archive/firefox-2009-09.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox/2010-01/", "privacy/archive/firefox-2010-01.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox/2010-12/", "privacy/archive/firefox-2010-12.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox/2011-06/", "privacy/archive/firefox-2011-06.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox/2012-06/", "privacy/archive/firefox-2012-06.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox/2012-09/", "privacy/archive/firefox-2012-09.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox/2012-12/", "privacy/archive/firefox-2012-12.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox/2013-05/", "privacy/archive/firefox-2013-05.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox-cliqz/2018-06/", "privacy/archive/firefox-cliqz-2018-06.html", ftl_files=["privacy/index"], active_locales=["de", "en-US"]),
    page(
        "archive/firefox-marketplace/2015-01/",
        "privacy/archive/firefox-marketplace-2015-01.html",
        ftl_files=["privacy/index"],
        active_locales=["de", "en-US"],
    ),
    page("archive/firefox/third-party/", "privacy/archive/firefox-third-party.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/hello/2014-11/", "privacy/archive/hello-2014-11.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/hello/2016-03/", "privacy/archive/hello-2016-03.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/thunderbird/2010-06/", "privacy/archive/thunderbird-2010-06.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/websites/2013-08/", "privacy/archive/websites-2013-08.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/persona/2017-07/", "privacy/archive/persona-2017-07.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox-os/2022-05/", "privacy/archive/firefox-os-2022-05.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/firefox-relay/2022-10/", "privacy/archive/firefox-relay-2022-10.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/mozilla-vpn/2022-10/", "privacy/archive/mozilla-vpn-2022-10.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page("archive/facebook/2023-04/", "privacy/archive/facebook-2023-04.html", ftl_files=["privacy/index"], active_locales=["en-US"]),
    page(
        "archive/firefox-private-network/notice-2023-06/",
        "privacy/archive/firefox-private-network-notice-2023-06.html",
        ftl_files=["privacy/index"],
        active_locales=["en-US"],
    ),
    page(
        "archive/firefox-private-network/tos-2023-06/",
        "privacy/archive/firefox-private-network-tos-2023-06.html",
        ftl_files=["privacy/index"],
        active_locales=["en-US"],
    ),
    page(
        "archive/firefox-betterweb/2023-06/",
        "privacy/archive/firefox-betterweb-2023-06.html",
        ftl_files=["privacy/index"],
        active_locales=["en-US"],
    ),
    page(
        "archive/firefox-fire-tv/2023-06/",
        "privacy/archive/firefox-fire-tv-2023-06.html",
        ftl_files=["privacy/index"],
        active_locales=["en-US"],
    ),
    page(
        "archive/firefox-reality/notice-2023-06/",
        "privacy/archive/firefox-reality-notice-2023-06.html",
        ftl_files=["privacy/index"],
        active_locales=["en-US"],
    ),
    page(
        "archive/firefox-reality/tos-2023-06/",
        "privacy/archive/firefox-reality-tos-2023-06.html",
        ftl_files=["privacy/index"],
        active_locales=["en-US"],
    ),
    page(
        "archive/firefox-monitor/2024-02/",
        "privacy/archive/firefox-monitor-2024-02.html",
        ftl_files=["privacy/index"],
        active_locales=["en-US"],
    ),
    page(
        "archive/mozilla-hubs/tos-2024-06/",
        "privacy/archive/mozilla-hubs-tos-2024-06.html",
        ftl_files=["privacy/index"],
        active_locales=["en-US"],
    ),
    page(
        "archive/mozilla-hubs/notice-2024-06/",
        "privacy/archive/mozilla-hubs-notice-2024-06.html",
        ftl_files=["privacy/index"],
        active_locales=["en-US"],
    ),
)
