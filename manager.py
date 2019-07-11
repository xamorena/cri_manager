import logging
import sys

LOG_FORMAT = '%(levelname)s @ %(asctime)s - %(name)s: %(message)s'
LOG_LEVEL = logging.DEBUG

def main():
    manager = None
    try:
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--cfgfile", type=str, default="etc/config.json", help="configuration file" )
        parser.add_argument("-l", "--logfile", type=str, default="logs/cri_manager.log", help="logging file" )
        parser.add_argument("-v", "--verbose", action="store_true", help="display information")
        args = parser.parse_args()
        logging.basicConfig(filename=args.logfile, level=LOG_LEVEL)
        logger = logging.getLogger()
        logger.setLevel(LOG_LEVEL)
        log_handler = logging.StreamHandler(sys.stdout)
        log_handler.setLevel(LOG_LEVEL)
        log_formatter = logging.Formatter(LOG_FORMAT)
        log_handler.setFormatter(log_formatter)
        logger.addHandler(log_handler)
        from cri_manager import CriManager
        from cri_manager import CriManagerConfiguration
        manager = CriManager(config=CriManagerConfiguration(filename=args.cfgfile))
        logger.info("CRI Manager: cri_manager release 1.0 is running on {}".format("localhost"))
        manager.start()
        logger.info("Creating services busybox echo 'hello world'")
        svc1 = manager.create_service('demo1', image='busybox', command=['echo', 'hello world'])
        svc2 = manager.api_create_service('demo2', image='busybox', command=['echo', 'hello world'])

    except Exception as err:
        logging.error("Error: {}".format(err))
    except KeyboardInterrupt:
        pass
    finally:
        logging.info('Bye!')

if __name__ == "__main__":
    main()
