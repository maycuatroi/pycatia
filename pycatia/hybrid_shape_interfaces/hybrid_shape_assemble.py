#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeAssemble(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeAssemble
                | 
                | Represents the hybrid shape assemble feature object.
                | Role: To access the data of the hybrid shape assemble feature object. This data
                | includes:
                | 
                |     A list of the assembled elements
                |     Some methods to access this data
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeAssemble
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_assemble = com_object

    @property
    def invert(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Invert() As boolean
                | 
                |     Returns or sets the invert mode.
                |     Legal values: True the result is inverted. False the result is not
                |     inverted.
                | 
                |     Example:
                | 
                |           This example sets the invert mode of
                |          the HybShpAssemble hybrid shape assemble feature to
                |          True.
                |          
                | 
                |          HybShpAssemble.Invert = True

        :return: bool
        """

        return self.hybrid_shape_assemble.Invert

    @invert.setter
    def invert(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_assemble.Invert = value

    def add_element(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddElement(Reference iElement)
                | 
                |     Adds an element to the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iElement
                |             The element to add to the hybrid shape assemble feature
                |             object.
                |             Sub-element(s) supported (see 
                | 
                |         Boundary object): Face, TriDimFeatEdge and BiDimFeatEdge.
                |         
                | 
                | Examples:
                |     The following example adds the iElement feature object to the
                |     HybridShapeAssemble object.
                | 
                |      HybridShapeAssemble.AddElement iElement

        :param Reference i_element:
        :return: None
        """
        return self.hybrid_shape_assemble.AddElement(i_element.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_element'
        # # vba_code = """
        # # Public Function add_element(hybrid_shape_assemble)
        # #     Dim iElement (2)
        # #     hybrid_shape_assemble.AddElement iElement
        # #     add_element = iElement
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_sub_element(self, i_sub_element):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AddSubElement(Reference iSubElement)
                | 
                |     Adds a sub element to the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iSubElement
                |             The sub element to remove to the hybrid shape assemble feature
                |             object.

        :param Reference i_sub_element:
        :return: None
        """
        return self.hybrid_shape_assemble.AddSubElement(i_sub_element.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_sub_element'
        # # vba_code = """
        # # Public Function add_sub_element(hybrid_shape_assemble)
        # #     Dim iSubElement (2)
        # #     hybrid_shape_assemble.AddSubElement iSubElement
        # #     add_sub_element = iSubElement
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def append_federated_element(self, i_element):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub AppendFederatedElement(Reference iElement)
                | 
                |     Appends an init to the list of elements to federate.
                | 
                |     Parameters:
                | 
                |         iElement
                |             Element to append. 
                | 
                |     See also:
                |         Reference

        :param Reference i_element:
        :return: None
        """
        return self.hybrid_shape_assemble.AppendFederatedElement(i_element.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'append_federated_element'
        # # vba_code = """
        # # Public Function append_federated_element(hybrid_shape_assemble)
        # #     Dim iElement (2)
        # #     hybrid_shape_assemble.AppendFederatedElement iElement
        # #     append_federated_element = iElement
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_angular_tolerance(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetAngularTolerance() As double
                | 
                |     Get the angular tolerance.
                | 
                |     Parameters:
                | 
                |         oValue
                |             The angular tolerance.

        :return: float
        """
        return self.hybrid_shape_assemble.GetAngularTolerance()

    def get_angular_tolerance_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetAngularToleranceMode() As boolean
                | 
                |     Get the angular tolerance mode.
                | 
                |     Parameters:
                | 
                |         oValue
                |             The angular tolerance mode.

        :return: bool
        """
        return self.hybrid_shape_assemble.GetAngularToleranceMode()

    def get_connex(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetConnex() As boolean
                | 
                |     Get the connex checker flag.
                | 
                |     Parameters:
                | 
                |         oConnex

        :return: bool
        """
        return self.hybrid_shape_assemble.GetConnex()

    def get_deviation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetDeviation() As double
                | 
                |     Get the deviation value.
                | 
                |     Parameters:
                | 
                |         odeviation
                |             The deviation.

        :return: float
        """
        return self.hybrid_shape_assemble.GetDeviation()

    def get_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetElement(long iRank) As Reference
                | 
                |     Retrieves an element used by the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the element to read. 
                | 
                |     Examples:
                |         The following example gets the oElement feature object of the
                |         HybridShapeAssemble object at the position iRank.
                | 
                |          Dim oElement As Reference
                |          Set oElement = HybridShapeAssemble.GetElement (iRank).

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.hybrid_shape_assemble.GetElement(i_rank))

    def get_elements_size(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetElementsSize() As long
                | 
                |     Returns the size of the list of elements to assemble in the hybrid shape
                |     assemble feature object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of elements in the Assemble.
                | 
                |             Example:
                |                 This example retrieves the number of elements in the
                |                 HybShpAssemble hybrid shape assemble.
                | 
                |                  Dim oSize As  long
                |                  oSize = HybShpAssemble.GetElementsSize

        :return: int
        """
        return self.hybrid_shape_assemble.GetElementsSize()

    def get_federated_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFederatedElement(long iRank) As Reference
                | 
                |     Retrieves an federated inits used by the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the element to read. 
                |         oElement
                |             The federated element. 
                | 
                |     See also:
                |         Reference

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.hybrid_shape_assemble.GetFederatedElement(i_rank))

    def get_federated_elements_size(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFederatedElementsSize() As long
                | 
                |     Gets the number of federated inits.
                | 
                |     Parameters:
                | 
                |         Size
                |             Number of elements.

        :return: int
        """
        return self.hybrid_shape_assemble.GetFederatedElementsSize()

    def get_federation_propagation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetFederationPropagation() As long
                | 
                |     Gets the propagation mode of the federation.
                | 
                |     Parameters:
                | 
                |         i
                |             type of propagation (0: No, 1: All, 2: Continuity,
                |             3:Tangency).

        :return: int
        """
        return self.hybrid_shape_assemble.GetFederationPropagation()

    def get_manifold(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetManifold() As boolean
                | 
                |     Get the manifold checker flag.
                | 
                |     Parameters:
                | 
                |         oManifold

        :return: bool
        """
        return self.hybrid_shape_assemble.GetManifold()

    def get_simplify(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetSimplify() As boolean
                | 
                |     Get the simplify flag.
                | 
                |     Parameters:
                | 
                |         oSimplify

        :return: bool
        """
        return self.hybrid_shape_assemble.GetSimplify()

    def get_sub_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetSubElement(long iRank) As Reference
                | 
                |     Retrieves a sub element used by the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the subelement to read.

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.hybrid_shape_assemble.GetSubElement(i_rank))

    def get_sub_elements_size(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetSubElementsSize() As long
                | 
                |     Returns the size of the list of sub-elements to remove in the hybrid shape
                |     assemble feature object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of sub elements in the Assemble.
                | 
                |             Example:
                |                 This example retrieves the number of sub elements in the
                |                 HybShpAssemble hybrid shape assemble.
                | 
                |                  Dim oSize As  long
                |                  oSize = HybShpAssemble.GetSubElementsSize

        :return: int
        """
        return self.hybrid_shape_assemble.GetSubElementsSize()

    def get_suppress_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetSuppressMode() As boolean
                | 
                |     Get the SuppressMode flag.
                | 
                |     Parameters:
                | 
                |         oSuppressMode

        :return: bool
        """
        return self.hybrid_shape_assemble.GetSuppressMode()

    def get_tangency_continuity(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetTangencyContinuity() As boolean
                | 
                |     Get the tangency continuity checker flag.
                | 
                |     Parameters:
                | 
                |         oTangencyContinuity

        :return: bool
        """
        return self.hybrid_shape_assemble.GetTangencyContinuity()

    def remove_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveElement(long iRank)
                | 
                |     Removes an element used by the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the element to remove. 
                | 
                |     Examples:
                |         The following example removes the feature object from the
                |         HybridShapeAssemble object at the position iRank.
                | 
                |          HybridShapeAssemble.RemoveElement iRank.

        :param int i_rank:
        :return: None
        """
        return self.hybrid_shape_assemble.RemoveElement(i_rank)

    def remove_federated_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveFederatedElement(long iRank)
                | 
                |     Removes an element to the list of elements to federate.
                | 
                |     Parameters:
                | 
                |         iRank
                |             Position of the element to remove.

        :param int i_rank:
        :return: None
        """
        return self.hybrid_shape_assemble.RemoveFederatedElement(i_rank)

    def remove_sub_element(self, i_rank):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub RemoveSubElement(long iRank)
                | 
                |     Removes a sub element used by the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the element to remove.

        :param int i_rank:
        :return: None
        """
        return self.hybrid_shape_assemble.RemoveSubElement(i_rank)

    def replace_element(self, i_pos, i_element):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub ReplaceElement(long iPos,
                | Reference iElement)
                | 
                |     Replaces the element at specified position in the hybrid shape assemble
                |     feature object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             Position at which the element should be replaced. 
                |         iElement
                |             Reference of the element to be inserted.
                | 
                |             Example:
                |                 This example replaces the element in the HybShpAssemble
                |                 assemble feature at specified position iPos
                | 
                |                  HybShpAssemble.ReplaceElement iPos,iElement

        :param int i_pos:
        :param Reference i_element:
        :return: None
        """
        return self.hybrid_shape_assemble.ReplaceElement(i_pos, i_element.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'replace_element'
        # # vba_code = """
        # # Public Function replace_element(hybrid_shape_assemble)
        # #     Dim iPos (2)
        # #     hybrid_shape_assemble.ReplaceElement iPos
        # #     replace_element = iPos
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_angular_tolerance(self, i_value):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetAngularTolerance(double iValue)
                | 
                |     Set the angular tolerance.
                | 
                |     Parameters:
                | 
                |         iValue
                |             The angular tolerance.

        :param float i_value:
        :return: None
        """
        return self.hybrid_shape_assemble.SetAngularTolerance(i_value)

    def set_angular_tolerance_mode(self, i_value):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetAngularToleranceMode(boolean iValue)
                | 
                |     Set the angular tolerance mode.
                | 
                |     Parameters:
                | 
                |         iValue
                |             The angular tolerance mode.

        :param bool i_value:
        :return: None
        """
        return self.hybrid_shape_assemble.SetAngularToleranceMode(i_value)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_angular_tolerance_mode'
        # # vba_code = """
        # # Public Function set_angular_tolerance_mode(hybrid_shape_assemble)
        # #     Dim iValue (2)
        # #     hybrid_shape_assemble.SetAngularToleranceMode iValue
        # #     set_angular_tolerance_mode = iValue
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_connex(self, i_connex):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetConnex(boolean iConnex)
                | 
                |     Set the connex checker flag.
                | 
                |     Parameters:
                | 
                |         iConnex

        :param bool i_connex:
        :return: None
        """
        return self.hybrid_shape_assemble.SetConnex(i_connex)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_connex'
        # # vba_code = """
        # # Public Function set_connex(hybrid_shape_assemble)
        # #     Dim iConnex (2)
        # #     hybrid_shape_assemble.SetConnex iConnex
        # #     set_connex = iConnex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_deviation(self, ideviation):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetDeviation(double ideviation)
                | 
                |     Set the deviation value.
                | 
                |     Parameters:
                | 
                |         ideviation
                |             The deviation.

        :param float ideviation:
        :return: None
        """
        return self.hybrid_shape_assemble.SetDeviation(ideviation)

    def set_federation_propagation(self, i_mode):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetFederationPropagation(long iMode)
                | 
                |     Sets the propagation mode of federation.
                | 
                |     Parameters:
                | 
                |         i
                |             type of propagation (0: No, 1: All, 2: Continuity,
                |             3:Tangency).

        :param int i_mode:
        :return: None
        """
        return self.hybrid_shape_assemble.SetFederationPropagation(i_mode)

    def set_manifold(self, i_manifold):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetManifold(boolean iManifold)
                | 
                |     Set the manifold checker flag.
                | 
                |     Parameters:
                | 
                |         iManifold

        :param bool i_manifold:
        :return: None
        """
        return self.hybrid_shape_assemble.SetManifold(i_manifold)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_manifold'
        # # vba_code = """
        # # Public Function set_manifold(hybrid_shape_assemble)
        # #     Dim iManifold (2)
        # #     hybrid_shape_assemble.SetManifold iManifold
        # #     set_manifold = iManifold
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_simplify(self, i_simplify):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetSimplify(boolean iSimplify)
                | 
                |     Set the simplify flag.
                | 
                |     Parameters:
                | 
                |         iSimplify

        :param bool i_simplify:
        :return: None
        """
        return self.hybrid_shape_assemble.SetSimplify(i_simplify)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_simplify'
        # # vba_code = """
        # # Public Function set_simplify(hybrid_shape_assemble)
        # #     Dim iSimplify (2)
        # #     hybrid_shape_assemble.SetSimplify iSimplify
        # #     set_simplify = iSimplify
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_suppress_mode(self, i_suppress_mode):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetSuppressMode(boolean iSuppressMode)
                | 
                |     Set the SuppressMode flag.
                | 
                |     Parameters:
                | 
                |         iSuppressMode

        :param bool i_suppress_mode:
        :return: None
        """
        return self.hybrid_shape_assemble.SetSuppressMode(i_suppress_mode)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_suppress_mode'
        # # vba_code = """
        # # Public Function set_suppress_mode(hybrid_shape_assemble)
        # #     Dim iSuppressMode (2)
        # #     hybrid_shape_assemble.SetSuppressMode iSuppressMode
        # #     set_suppress_mode = iSuppressMode
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tangency_continuity(self, i_tangency_continuity):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetTangencyContinuity(boolean iTangencyContinuity)
                | 
                |     Set the tangency continuity checker flag.
                | 
                |     Parameters:
                | 
                |         iTangencyContinuity

        :param bool i_tangency_continuity:
        :return: None
        """
        return self.hybrid_shape_assemble.SetTangencyContinuity(i_tangency_continuity)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_tangency_continuity'
        # # vba_code = """
        # # Public Function set_tangency_continuity(hybrid_shape_assemble)
        # #     Dim iTangencyContinuity (2)
        # #     hybrid_shape_assemble.SetTangencyContinuity iTangencyContinuity
        # #     set_tangency_continuity = iTangencyContinuity
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeAssemble(name="{ self.name }")'