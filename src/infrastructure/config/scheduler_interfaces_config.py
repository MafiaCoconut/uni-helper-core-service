from infrastructure.interfaces_impl.scheduler_interface_impl import SchedulerInterfaceImpl


def get_scheduler_interface() -> SchedulerInterfaceImpl:
    return SchedulerInterfaceImpl()

