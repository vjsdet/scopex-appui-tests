from ui.src.PlatformConfig import PlatformConfig
import logging
import pdb as pd

from ui.src.pages.sign_in import SigninAppPage

log = logging.getLogger(__name__)


class WalkThrough:
    status = None


def _open_app(context, platform_name='Android'):
    """
    create appium driver instance and returns back launch status
    """

    app_launch = PlatformConfig().open_app(platform_name, reset=True)
    (lambda: context.page.launch_app() if not app_launch else None)()
    return app_launch


def run_app(context, platform_name: str, fresh: bool = True):
    log.info(f"Running run_app with platform name {platform_name} and with fresh start as {fresh}")
    first_launch = _open_app(context, platform_name)
    if not first_launch:
        _open_app(context, platform_name)


def after_feature(context, feature):
    log.info(f"********* {feature} ********* feature execution completed with status= {feature.status}")


def after_scenario(context, scenario):
    log.info(f"********* {scenario} ********* scenario execution completed with status= {scenario.status}")
    SigninAppPage().close_relaunch_app()


def before_feature(context, feature):
    log.info(f"******* {feature} ****** feature execution started= {feature.status}")
    _open_app(context)


def before_scenario(context, scenario):
    log.info("Checking walkthrough screen visible")
    if WalkThrough.status is None:
        WalkThrough.status = SigninAppPage().skip_walkthrough()
    elif WalkThrough.status:
        SigninAppPage().click_on_skip_button()
